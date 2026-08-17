#!/usr/bin/env python3
"""Prueft, ob in wissen/ Text verloren gegangen ist.

Vergleicht jeden sichtbaren Textknoten aus <main> der HTML-Dateien gegen den
gesammelten Text aus tools/wissen_inhalt.json. Laeuft sowohl gegen die alten
Tailwind-Seiten (Beweis, dass die Extraktion vollstaendig war) als auch gegen
die neu gerenderten Seiten (Beweis, dass das Redesign nichts verschluckt hat).
"""
import html
import json
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absichtlich streng: ein einzelnes "<" im Fliesstext (z. B. "Natrium < 2,3 g")
# wuerde bei <[^>]+> alles bis zum naechsten ">" verschlucken und echten Text
# als vermeintlichen Verlust verstecken.
TAG = re.compile(r'</?[a-zA-Z][^<>]*>')
KOMMENTAR = re.compile(r'<!--.*?-->', re.S)
# Die Brotkrume ist Navigation wie Kopfleiste und Fuss: feste Beschriftungen
# plus der Seitenname. Sie steht deshalb nicht in der Inhalts-JSON.
KRUME = re.compile(r'<p class="krume">.*?</p>', re.S)


def norm(x):
    return re.sub(r'\s+', ' ', html.unescape(TAG.sub(' ', x))).strip()


def json_text(d):
    teile = []

    def geh(o):
        if isinstance(o, str):
            teile.append(o)
        elif isinstance(o, list):
            for v in o:
                geh(v)
        elif isinstance(o, dict):
            for v in o.values():
                geh(v)

    geh(d)
    return norm(' '.join(teile))


def main():
    daten = {d['slug']: d for d in json.load(
        open(os.path.join(WURZEL, 'tools', 'wissen_inhalt.json'), encoding='utf-8'))}
    daten['index'] = json.load(
        open(os.path.join(WURZEL, 'tools', 'wissen_index.json'), encoding='utf-8'))
    wissen = os.path.join(WURZEL, 'wissen')
    gesamt = 0
    fehlend = []
    for f in sorted(os.listdir(wissen)):
        if not f.endswith('.html'):
            continue
        s = open(os.path.join(wissen, f), encoding='utf-8').read()
        # Inhaltsbereich ohne Kopfleiste, Menue und Fuss - die stehen bewusst
        # nicht in der JSON. Alte Tailwind-Seiten beginnen bei <main>, die neuen
        # beim Seitenkopf, der die h1 traegt.
        start = s.find('<section class="masthead"')
        if start < 0:
            start = s.index('<main id="main">')
        haupt = s[start:s.index('<footer')]
        haupt = re.sub(r'<script.*?</script>', '', haupt, flags=re.S)
        haupt = KOMMENTAR.sub('', haupt)
        haupt = KRUME.sub('', haupt)
        neu = json_text(daten[f[:-5]])
        for roh in TAG.split(haupt):
            t = norm(roh)
            if len(t) < 10:
                continue
            gesamt += 1
            # Manche Beschriftungen setzen zwei JSON-Werte mit Mittelpunkt
            # zusammen ("ICD K58 · 12 Quellen"). Zusammensetzen ist kein
            # Erfinden, solange jeder Teil aus der JSON stammt.
            if t not in neu and not all(p in neu for p in t.split(' · ')):
                fehlend.append((f, t))
    print('Textknoten geprueft: %d, nicht wiedergefunden: %d' % (gesamt, len(fehlend)))
    for f, t in fehlend:
        print('  %-42s %s' % (f, t[:110]))
    schief = struktur_pruefen(daten)
    return 1 if fehlend or schief else 0


def struktur_pruefen(daten):
    """Zaehlt div-Klammern im Artikeltext.

    Ein einzelnes verwaistes </div> kostet keinen Buchstaben und faellt der
    Textpruefung deshalb nicht auf - es schliesst aber das Layoutraster zu
    frueh, und die Randspalte mit Verzeichnis und Terminkarte rutscht aus dem
    Artikel heraus. Genau das ist einmal passiert, in allen 21 Artikeln.
    """
    schief = []
    for slug, d in sorted(daten.items()):
        for s in d.get('abschnitte', []):
            auf = len(re.findall(r'<div\b', s['html']))
            zu = len(re.findall(r'</div>', s['html']))
            if auf != zu:
                schief.append((slug, s['id'], auf, zu))
    print('div-Klammern: %d Abschnitte unausgeglichen' % len(schief))
    for slug, sid, auf, zu in schief:
        print('  %-42s %-30s auf=%d zu=%d' % (slug, sid, auf, zu))
    return schief


if __name__ == '__main__':
    sys.exit(main())
