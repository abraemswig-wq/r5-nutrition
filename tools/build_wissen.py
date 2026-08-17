#!/usr/bin/env python3
"""Baut die Fachartikel unter wissen/ aus tools/wissen_inhalt.json.

Der Inhalt kommt ausschliesslich aus der JSON, die Seitenhuelle (Consent,
Kopfleiste, Menue, Fuss) wird aus programme.html gelesen. So gibt es je eine
Wahrheit: den Text in der JSON, das Design im uebrigen Seitenbestand. Wer die
Navigation aendert, aendert sie einmal.

  python3 tools/build_wissen.py
"""
import html
import json
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VORLAGE = os.path.join(WURZEL, 'programme.html')
JSON = os.path.join(WURZEL, 'tools', 'wissen_inhalt.json')
WISSEN = os.path.join(WURZEL, 'wissen')

TAG = re.compile(r'</?[a-zA-Z][^<>]*>')

# Die Sprungmarken liegen seit dem Umbau auf den Unterseiten, nicht mehr auf der
# Startseite. Ohne diese Karte zeigen 176 Verweise ins Leere.
ANKER = {
    '../#anmelden': '../programme.html#anmelden',
    '../#programme': '../programme.html#programme',
    '../#preise': '../programme.html#preise',
    '../#ablauf': '../programme.html#ablauf',
    '../#konzept': '../programme.html#konzept',
    '../#indikationen': '../programme.html#indikationen',
    '../#faq': '../programme.html#faq',
    '../#standort': '../standort.html#standort',
}

# Wie lang eine ausgestanzte Zeile hoechstens sein darf. Der Cream-Block bricht
# nicht um (white-space:pre); bei 36 Zeichen stuende der Titel auf dem Handy
# ausserhalb des Bildes. Also vorher an Wortgrenzen aufteilen.
ZEILE_MAX = 18


def anker_ersetzen(s):
    for alt, neu in ANKER.items():
        s = s.replace('href="%s"' % alt, 'href="%s"' % neu)
    return s


def ziel_von(href):
    return ANKER.get(href, href)


def huelle():
    """Consent-Block, Schriften, Kopfleiste, Menue und Fuss aus programme.html."""
    s = open(VORLAGE, encoding='utf-8').read()
    consent = s[s.index('<!DOCTYPE html>'):s.index('  <meta charset=')]
    # Nur bis zur Schriftzeile: Stylesheets, das js-Flag und das Buchungsskript
    # setzt die Vorlage unten selbst, sonst stuenden sie doppelt im Kopf.
    kopf_ende = s[s.index('  <!-- Favicons -->'):
                  s.index('  <link rel="stylesheet" href="css/seite.css"')]
    chrome = s[s.index('<a href="#inhalt" class="sr">'):s.index('<section class="masthead"')]
    fuss = s[s.index('<footer class="page-foot"'):s.index('</body>')]

    def hoch(x):
        x = re.sub(r'href="(programme|team|unternehmen|standort|impressum|datenschutz|index)\.html',
                   r'href="../\1.html', x)
        x = x.replace('href="wissen/"', 'href="./"')
        x = x.replace('src="R5-Logo', 'src="../R5-Logo')
        x = x.replace('href="fonts.css"', 'href="../fonts.css"')
        x = x.replace('src="js/seite.js"', 'src="../js/seite.js"')
        x = x.replace('href="?dmropen=1"', 'href="../programme.html?dmropen=1"')
        # Der Fuss verweist auf Marken, die seit dem Umbau auf programme.html
        # liegen; ohne Praefix landet man auf der Artikelseite selbst.
        x = re.sub(r'href="#(programme|indikationen|preise|ablauf|konzept|kassen-check|anmelden)"',
                   r'href="../programme.html#\1"', x)
        return x

    chrome = hoch(chrome)
    chrome = chrome.replace('<a href="../programme.html" aria-current="page">',
                            '<a href="../programme.html">')
    chrome = chrome.replace('<a href="./">Wissen</a>',
                            '<a href="./" aria-current="page">Wissen</a>', 1)
    return consent, hoch(kopf_ende), chrome, hoch(fuss)


def zeilen(h1_html):
    """h1-Markup in ausgestanzte Zeilen zerlegen."""
    roh = [html.unescape(TAG.sub('', t)).strip()
           for t in re.split(r'<br\s*/?>', h1_html)]
    aus = []
    for teil in [t for t in roh if t]:
        zeile = ''
        for wort in teil.split():
            kandidat = (zeile + ' ' + wort).strip()
            if zeile and len(kandidat) > ZEILE_MAX:
                aus.append(zeile)
                zeile = wort
            else:
                zeile = kandidat
        if zeile:
            aus.append(zeile)
    return aus


def hl(text, klasse='hl hl--klein'):
    """Ueberschrift als ausgestanzte Zeilen - auch h2 muss umbrechen.

    Ein einzelner Block mit 47 Zeichen ("Bereit, dein Low-FODMAP strukturiert
    anzugehen?") stuende auf dem Handy weit ausserhalb des Bildes.
    """
    return '<h2 class="%s">\n%s\n    </h2>' % (klasse, '\n'.join(
        '      <span class="hl__line">%s</span>' % esc(z) for z in zeilen(text)))


def esc(x):
    """Nur fuer Text, der vorher entschluesselt wurde (die h1-Zeilen).

    Alle anderen Werte stammen unveraendert aus dem alten Markup und tragen
    ihre Entitaeten bereits - ein zweites Escaping machte aus "&" ein "&amp;".
    """
    return html.escape(x, quote=True)


def bauen(a, consent, kopf_ende, chrome, fuss):
    slug = a['slug']
    hero = a['hero']

    h1 = '\n'.join('    <span class="hl__line">%s</span>' % esc(z)
                   for z in zeilen(hero['h1_html']))
    krume = ('<p class="krume"><a href="../">Startseite</a> · <a href="./">Wissen</a> · '
             '<span>%s</span></p>' % hero['breadcrumb'])
    icd = '<p class="icd rv">%s</p>' % hero['icd_pill'] if hero['icd_pill'] else ''
    meta = ''.join('<span>%s</span>' % m for m in hero['meta_zeile'])

    toc = '\n'.join('        <li><a href="%s">%s</a></li>' % (t['href'], t['label'])
                    for t in a['toc'])

    koerper = []
    for s in a['abschnitte']:
        koerper.append('  <h2 id="%s">%s</h2>' % (s['id'], s['titel']))
        koerper.append(anker_ersetzen(s['html']))

    faq = '\n'.join(
        '      <details>\n'
        '        <summary>%s</summary>\n'
        '        <p class="faq__a">%s</p>\n'
        '      </details>' % (f['frage'], anker_ersetzen(f['antwort']))
        for f in a['faq']['fragen'])

    quellen = '\n'.join('      <li id="%s">%s</li>' % (q['id'], q['html'])
                        for q in a['quellen']['quellen'])
    vorspann = ('\n    <p class="lede lede--breit rv">%s</p>' % a['quellen']['vorspann']
                if a['quellen'].get('vorspann') else '')
    disclaimer = ''
    if a['quellen'].get('disclaimer'):
        disclaimer = ('\n    <p class="disclaimer rv"><b>%s</b>%s</p>'
                      % (a['quellen']['disclaimer_label'], a['quellen']['disclaimer']))

    verwandt = '\n'.join(
        '      <a class="lese rv" href="%s">\n'
        '        <span class="lese__k">%s</span>\n'
        '        <h3>%s</h3>\n'
        '        <p>%s</p>\n'
        '        <span class="lese__go">Lesen</span>\n'
        '      </a>' % (k['href'], k['pill'], k['titel'], k['text'])
        for k in a['verwandt']['karten'])

    cta = a['cta']
    knoepfe = '\n'.join(
        '      <a class="btn%s" href="%s">%s</a>'
        % ('' if i == 0 else ' btn--ghost', ziel_von(k['href']), k['text'])
        for i, k in enumerate(cta['knoepfe']))
    # Die Randkarte bekommt dieselben Beschriftungen wie der CTA-Block. Eigene
    # zu erfinden hiesse, dem Kunden etwas zu versprechen, das niemand freigegeben hat.
    artcard_l = '\n'.join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (ziel_von(k['href']),
           ' target="_blank" rel="noopener"' if k['href'].endswith('.pdf') else '',
           k['text'])
        for k in cta['knoepfe'])

    jsonld = '\n'.join('  <script type="application/ld+json">\n%s\n  </script>' % j
                       for j in a['jsonld'])

    return '''%(consent)s  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>%(title)s</title>
  <meta name="description" content="%(desc)s" />
  <meta name="keywords" content="%(keywords)s" />
  <meta name="author" content="REHAB FIVE GmbH" />
  <!-- Vorschau: bis die Domain entschieden ist, darf Google diese Seite nicht
       indexieren. tools/set_domain.py setzt das beim Go-live zurueck. -->
  <meta name="robots" content="%(robots)s" />
  <meta name="theme-color" content="#121815" />
  <link rel="canonical" href="%(canonical)s" />

  <meta property="og:type" content="article" />
  <meta property="og:locale" content="de_DE" />
  <meta property="og:site_name" content="REHAB FIVE NUTRITION" />
  <meta property="og:title" content="%(og_title)s" />
  <meta property="og:description" content="%(og_desc)s" />
  <meta property="og:url" content="%(og_url)s" />
  <meta property="og:image" content="%(og_image)s" />

%(kopf_ende)s  <link rel="stylesheet" href="../css/seite.css" />
  <link rel="stylesheet" href="../css/wissen.css" />
  <script>document.documentElement.classList.add('js')</script>
  <script async src="https://cdn.docmedico-rezeption.de/j9u4c9m7a/reception_embed.js"></script>

%(jsonld)s
</head>
<body class="page">

%(chrome)s<section class="masthead" data-abschnitt>
  <div class="masthead__inner">
    %(krume)s
    %(icd)s
    <h1 class="hl hl--klein">
%(hl)s
    </h1>
    <p class="lede lede--breit rv">%(sub)s</p>
    <p class="artmeta rv">%(meta)s</p>
  </div>
</section>

<main id="inhalt">

<div class="artbody">
  <article class="prose" data-abschnitt>
    <div class="tldr rv">
      <p class="tldr__label">%(quick_label)s</p>
      <p>%(quick)s</p>
    </div>

%(koerper)s
  </article>

  <aside class="artside" data-abschnitt>
    <nav class="toc" aria-label="Inhalt">
      <p class="toc__h">%(toc_label)s</p>
      <ol class="toc__l">
%(toc)s
      </ol>
    </nav>
    <div class="artcard rv">
      <p class="artcard__h">%(cta_eyebrow)s</p>
      <p class="artcard__t">%(cta_text)s</p>
      <ul class="artcard__l">
%(artcard_l)s
      </ul>
    </div>
  </aside>
</div>

<section class="abschnitt abschnitt--eng" id="faq" data-abschnitt>
  <div class="kopfzeile">
    <p class="kicker rv">%(faq_kicker)s</p>
    %(faq_titel)s
  </div>
  <div class="faq__list rv">
%(faq)s
  </div>
</section>

<section class="quellen" data-abschnitt>
  <p class="kicker rv">%(q_kicker)s</p>
  %(q_titel)s%(vorspann)s
  <ol class="quellen__l rv">
%(quellen)s
  </ol>%(disclaimer)s
</section>

<section class="abschnitt abschnitt--eng" data-abschnitt>
  <div class="kopfzeile">
    <p class="kicker rv">%(v_kicker)s</p>
    %(v_titel)s
  </div>
  <div class="lesen">
%(verwandt)s
  </div>
</section>

<section class="abschnitt tail" id="anmelden" data-abschnitt>
  <p class="kicker rv">%(cta_eyebrow)s</p>
  %(cta_titel)s
  <p class="lede rv">%(cta_text)s</p>
  <div class="btns rv">
%(knoepfe)s
  </div>
</section>

</main>

%(fuss)s
<script src="../js/seite.js" defer></script>
</body>
</html>
''' % {
        'consent': consent,
        'title': a['title'],
        'desc': a['meta_desc'],
        'keywords': a['keywords'] or '',
        'robots': a['robots'] or 'noindex, nofollow',
        'canonical': a['canonical'] or '',
        'og_title': a['og_title'] or a['title'],
        'og_desc': a['og_desc'] or a['meta_desc'],
        'og_url': a['og_url'] or a['canonical'] or '',
        'og_image': a['og_image'] or '',
        'kopf_ende': kopf_ende,
        'jsonld': jsonld,
        'chrome': chrome,
        'krume': krume,
        'icd': icd,
        'hl': h1,
        'sub': hero['subheading'],
        'meta': meta,
        'quick_label': a['quick']['eyebrow'],
        'quick': anker_ersetzen(a['quick']['html']),
        'koerper': '\n\n'.join(koerper),
        'toc_label': a['toc_label'],
        'toc': toc,
        'cta_eyebrow': cta['eyebrow'],
        'cta_titel': hl(cta['titel'], 'hl hl--klein hl--center'),
        'cta_text': anker_ersetzen(cta['text']),
        'faq_kicker': a['faq']['eyebrow'],
        'faq_titel': hl(a['faq']['titel']),
        'faq': faq,
        'q_kicker': a['quellen']['eyebrow'],
        'q_titel': hl(a['quellen']['titel']),
        'vorspann': vorspann,
        'quellen': quellen,
        'disclaimer': disclaimer,
        'v_kicker': a['verwandt']['eyebrow'],
        'v_titel': hl(a['verwandt']['titel']),
        'verwandt': verwandt,
        'knoepfe': knoepfe,
        'artcard_l': artcard_l,
        'fuss': fuss,
    }


def main():
    consent, kopf_ende, chrome, fuss = huelle()
    daten = json.load(open(JSON, encoding='utf-8'))
    for a in daten:
        ziel = os.path.join(WISSEN, a['slug'] + '.html')
        open(ziel, 'w', encoding='utf-8').write(bauen(a, consent, kopf_ende, chrome, fuss))
        print('geschrieben: wissen/%s.html' % a['slug'])
    print('\n%d Artikel gebaut.' % len(daten))


if __name__ == '__main__':
    sys.exit(main())
