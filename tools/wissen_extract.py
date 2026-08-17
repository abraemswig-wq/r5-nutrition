#!/usr/bin/env python3
"""Liest alle Fachartikel unter wissen/ in eine einzige Inhalts-JSON.

Hintergrund: build_wissen_articles.py kennt nur 14 der 21 Artikel, sieben
existieren ausschliesslich als HTML. Solange zwei Quellen nebeneinander
liegen, haelt jede Reparatur an den Seiten nur bis zum naechsten
Generatorlauf. Diese Datei zieht den Inhalt aus dem HTML heraus, damit die
JSON danach die einzige Wahrheit ist.
"""
import json
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WISSEN = os.path.join(WURZEL, 'wissen')
ZIEL = os.path.join(WURZEL, 'tools', 'wissen_inhalt.json')


def eins(muster, text, name, datei, flags=re.S):
    treffer = re.findall(muster, text, flags)
    if len(treffer) != 1:
        raise SystemExit('%s: %d Treffer fuer %s' % (datei, len(treffer), name))
    return treffer[0]


def vielleicht(muster, text, flags=re.S):
    m = re.search(muster, text, flags)
    return m.group(1).strip() if m else None


def text_von(html_fragment):
    t = re.sub(r'<[^>]+>', '', html_fragment)
    return re.sub(r'\s+', ' ', t).strip()


def kopf_lesen(s, datei):
    d = {}
    d['title'] = eins(r'<title>(.*?)</title>', s, 'title', datei)
    d['meta_desc'] = eins(r'<meta name="description" content="(.*?)"', s, 'description', datei)
    d['keywords'] = vielleicht(r'<meta name="keywords" content="(.*?)"', s)
    d['canonical'] = vielleicht(r'<link rel="canonical" href="(.*?)"', s)
    d['og_title'] = vielleicht(r'<meta property="og:title" content="(.*?)"', s)
    d['og_desc'] = vielleicht(r'<meta property="og:description" content="(.*?)"', s)
    d['og_image'] = vielleicht(r'<meta property="og:image" content="(.*?)"', s)
    d['og_url'] = vielleicht(r'<meta property="og:url" content="(.*?)"', s)
    d['robots'] = vielleicht(r'<meta name="robots" content="(.*?)"', s)
    d['jsonld'] = [b.strip() for b in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
    return d


def hero_lesen(s, datei):
    hero = eins(r'<section class="gradient-hero[^"]*">(.*?)</section>', s, 'hero', datei)
    d = {}
    krume = eins(r'<nav[^>]*class="text-xs text-white/60">(.*?)</nav>', hero, 'breadcrumb', datei)
    d['breadcrumb'] = text_von(vielleicht(r'<span class="text-white/85">(.*?)</span>', krume) or '')
    d['icd_pill'] = text_von(vielleicht(r'<p class="mt-6 inline-flex[^"]*">(.*?)</p>', hero) or '')
    d['h1_html'] = re.sub(
        r'\s*\n\s*', '', eins(r'<h1 class="display[^"]*">(.*?)</h1>', hero, 'h1', datei).strip())
    d['subheading'] = text_von(vielleicht(r'<p class="mt-5 text-lg text-white/85[^"]*">(.*?)</p>', hero) or '')
    zeile = vielleicht(r'<div class="mt-6 flex flex-wrap[^"]*text-white/60">(.*?)</div>', hero) or ''
    d['meta_zeile'] = [text_von(x) for x in re.findall(r'<span>(.*?)</span>', zeile, re.S)]
    return d


def quick_lesen(s, datei):
    block = eins(r'border-l-4 border-brand-500">(.*?)</div>', s, 'quick-answer', datei)
    return {
        'eyebrow': text_von(vielleicht(r'<p class="eyebrow[^"]*">(.*?)</p>', block) or ''),
        'html': (vielleicht(r'<p class="mt-3 text-lg md:text-xl[^"]*">(.*?)</p>', block) or ''),
    }


def artikel_lesen(s, datei):
    art = eins(r'<article class="prose-r5">(.*?)</article>', s, 'article', datei)
    toc_roh = eins(r'<nav aria-label="Inhalt".*?</nav>', art, 'toc', datei)
    toc = [{'href': h, 'label': text_von(t)}
           for h, t in re.findall(r'<li><a href="(#[^"]*)"[^>]*>(.*?)</a></li>', toc_roh, re.S)]
    toc_label = text_von(vielleicht(r'<p class="text-xs font-semibold uppercase[^"]*">(.*?)</p>', toc_roh) or '')

    rumpf = art[art.index(toc_roh) + len(toc_roh):]
    teile = re.split(r'\n\s*<h2 id="([^"]+)">(.*?)</h2>\n', rumpf, flags=re.S)
    vorspann = teile[0].strip()
    if vorspann:
        raise SystemExit('%s: Text vor der ersten h2: %r' % (datei, vorspann[:120]))
    abschnitte = []
    for i in range(1, len(teile), 3):
        abschnitte.append({
            'id': teile[i],
            'titel': teile[i + 1].strip(),
            'html': teile[i + 2].strip(),
        })
    if not abschnitte:
        raise SystemExit('%s: keine h2-Abschnitte' % datei)
    return {'toc_label': toc_label, 'toc': toc, 'abschnitte': abschnitte}


def cta_lesen(s, datei):
    block = eins(r'<section class="bg-forest-700 text-white">\s*<div class="max-w-4xl(.*?)\n    </section>',
                 s, 'cta', datei)
    knoepfe = [{'href': h, 'text': text_von(t)}
               for h, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)]
    return {
        'eyebrow': text_von(vielleicht(r'<p class="eyebrow[^"]*">(.*?)</p>', block) or ''),
        'titel': text_von(vielleicht(r'<h2 class="display[^"]*">(.*?)</h2>', block) or ''),
        'text': (vielleicht(r'<p class="mt-3 text-white/85">(.*?)</p>', block) or ''),
        'knoepfe': knoepfe,
    }


def faq_lesen(s, datei):
    block = eins(r'<section id="faq"(.*?)\n    </section>', s, 'faq', datei)
    fragen = []
    for roh in re.findall(r'<details[^>]*>(.*?)</details>', block, re.S):
        frage = eins(r'<summary[^>]*>(.*?)<span class="chev', roh, 'summary', datei)
        antwort = eins(r'</summary>\s*<p[^>]*>(.*?)</p>', roh, 'faq-antwort', datei)
        fragen.append({'frage': text_von(frage), 'antwort': antwort.strip()})
    return {
        'eyebrow': text_von(vielleicht(r'<p class="eyebrow[^"]*">(.*?)</p>', block) or ''),
        'titel': text_von(vielleicht(r'<h2 class="display[^"]*">(.*?)</h2>', block) or ''),
        'fragen': fragen,
    }


def quellen_lesen(s, datei):
    block = eins(r'<p class="eyebrow text-xs text-brand-600">Wissenschaftliche Quellen</p>(.*?)\n    </section>',
                 s, 'quellen', datei)
    quellen = [{'id': i, 'html': h.strip()}
               for i, h in re.findall(r'<li id="(q\d+)">(.*?)</li>', block, re.S)]
    disc = vielleicht(r'<p><strong>Medizinischer Disclaimer:</strong>(.*?)</p>', block)
    return {
        'eyebrow': 'Wissenschaftliche Quellen',
        'titel': text_von(vielleicht(r'<h2 class="display[^"]*"[^>]*>(.*?)</h2>', block) or ''),
        'vorspann': vielleicht(r'</h2>\s*<p class="mt-3 text-ink-700">(.*?)</p>', block),
        'quellen': quellen,
        'disclaimer_label': 'Medizinischer Disclaimer:',
        'disclaimer': disc.strip() if disc else None,
    }


def verwandt_lesen(s, datei):
    block = eins(r'<p class="eyebrow text-xs text-brand-600">Verwandte Indikationen</p>(.*?)\n    </section>',
                 s, 'verwandt', datei)
    karten = []
    for roh_href, roh in re.findall(r'<a href="([^"]+)"[^>]*class="group rounded-2xl(.*?)</a>', block, re.S):
        karten.append({
            'href': roh_href,
            'pill': text_von(vielleicht(r'<p class="text-xs font-semibold[^"]*">(.*?)</p>', roh) or ''),
            'titel': text_von(vielleicht(r'<h3[^>]*>(.*?)</h3>', roh) or ''),
            'text': text_von(vielleicht(r'<p class="mt-2 text-sm[^"]*">(.*?)</p>', roh) or ''),
        })
    return {
        'eyebrow': 'Verwandte Indikationen',
        'titel': text_von(vielleicht(r'<h2 class="display[^"]*"[^>]*>(.*?)</h2>', block) or ''),
        'karten': karten,
    }


def artikel(pfad):
    datei = os.path.basename(pfad)
    s = open(pfad, encoding='utf-8').read()
    d = {'slug': datei[:-5]}
    d.update(kopf_lesen(s, datei))
    d['hero'] = hero_lesen(s, datei)
    d['quick'] = quick_lesen(s, datei)
    d.update(artikel_lesen(s, datei))
    d['cta'] = cta_lesen(s, datei)
    d['faq'] = faq_lesen(s, datei)
    d['quellen'] = quellen_lesen(s, datei)
    d['verwandt'] = verwandt_lesen(s, datei)
    return d


def main():
    dateien = sorted(f for f in os.listdir(WISSEN)
                     if f.endswith('.html') and f != 'index.html')
    daten = []
    for f in dateien:
        daten.append(artikel(os.path.join(WISSEN, f)))
        print('gelesen: %s (%d Abschnitte, %d FAQ, %d Quellen)' % (
            f, len(daten[-1]['abschnitte']), len(daten[-1]['faq']['fragen']),
            len(daten[-1]['quellen']['quellen'])))
    with open(ZIEL, 'w', encoding='utf-8') as fh:
        json.dump(daten, fh, ensure_ascii=False, indent=2)
    print('\n%d Artikel -> %s' % (len(daten), ZIEL))


if __name__ == '__main__':
    sys.exit(main())
