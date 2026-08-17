#!/usr/bin/env python3
"""Baut wissen/index.html aus tools/wissen_index.json.

Teilt sich Huelle, Ankerkarte und Zeilenumbruch mit build_wissen.py - die
Uebersicht ist dieselbe Seite wie ein Artikel, nur mit anderem Rumpf.

Die Aufteilung in sieben ausfuehrliche und vierzehn kompakte Indikationen ist
redaktionell gewollt und bleibt: die sieben tragen Quick-Answer, Protokoll und
acht bis zwoelf Quellen, die vierzehn sind Kurzfassungen. Wer sie zu einer
Liste zusammenzieht, verspricht bei allen 21 dieselbe Tiefe.

  python3 tools/build_wissen_index.py
"""
import json
import os
import sys

from build_wissen import WURZEL, huelle, zeilen, esc, hl, ziel_von

JSON = os.path.join(WURZEL, 'tools', 'wissen_index.json')
ZIEL = os.path.join(WURZEL, 'wissen', 'index.html')


def bauen(d, consent, kopf_ende, chrome, fuss):
    kopfzeilen = '\n'.join('    <span class="hl__line">%s</span>' % esc(z)
                           for z in zeilen(d['h1_html']))
    checks = '\n'.join('      <li>%s</li>' % c.lstrip('✓ ') for c in d['checks'])

    top = '\n'.join(
        '      <a class="lese rv" href="%s">\n'
        '        <span class="lese__k">%s · %s</span>\n'
        '        <h3>%s</h3>\n'
        '        <p>%s</p>\n'
        '        <span class="lese__go">%s</span>\n'
        '      </a>' % (k['href'], k['icd'], k['quellen'], k['titel'], k['text'], k['go'])
        for k in d['top']['karten'])

    weitere = '\n'.join(
        '      <li><a href="%s"><b>%s</b><span>%s</span></a></li>'
        % (k['href'], k['titel'], k['icd'])
        for k in d['weitere']['karten'])

    jsonld = '\n'.join('  <script type="application/ld+json">\n%s\n  </script>' % j
                       for j in d['jsonld'])

    return '''%(consent)s  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>%(title)s</title>
  <meta name="description" content="%(desc)s" />
  <meta name="author" content="REHAB FIVE GmbH" />
  <!-- Vorschau: bis die Domain entschieden ist, darf Google diese Seite nicht
       indexieren. tools/set_domain.py setzt das beim Go-live zurueck. -->
  <meta name="robots" content="%(robots)s" />
  <meta name="theme-color" content="#121815" />
  <link rel="canonical" href="%(canonical)s" />

  <meta property="og:type" content="website" />
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
    <p class="krume"><a href="../">Startseite</a> · <span>%(krume)s</span></p>
    <div class="kopfzeile">
    <p class="kicker rv">%(pill)s</p>
    <h1 class="hl">
%(kopfzeilen)s
    </h1>
    <p class="lede lede--breit rv">%(sub)s</p>
    <ul class="checks rv">
%(checks)s
    </ul>
    </div>
  </div>
</section>

<main id="inhalt">

<section class="abschnitt" id="top" data-abschnitt>
  <div class="kopfzeile">
    <p class="kicker rv">%(top_kicker)s</p>
    %(top_titel)s
    <p class="lede lede--breit rv">%(top_text)s</p>
  </div>

  <div class="lesen">
%(top)s
  </div>
</section>

<section class="abschnitt abschnitt--rand" id="weitere" data-abschnitt>
  <div class="kopfzeile">
    <p class="kicker rv">%(w_kicker)s</p>
    %(w_titel)s
    <p class="lede lede--breit rv">%(w_text)s</p>
  </div>

  <ul class="weiter__l rv">
%(weitere)s
  </ul>
</section>

</main>

<section class="tail" id="anmelden" data-abschnitt>
  %(cta_titel)s
  <p class="lede rv">%(cta_text)s</p>
  <div class="btns rv">
    <a class="btn" href="%(cta_href)s">%(cta_knopf)s</a>
  </div>
</section>

%(fuss)s
<script src="../js/seite.js" defer></script>
</body>
</html>
''' % {
        'consent': consent,
        'title': d['title'],
        'desc': d['meta_desc'],
        'robots': d['robots'] or 'noindex, nofollow',
        'canonical': d['canonical'] or '',
        'og_title': d['og_title'] or d['title'],
        'og_desc': d['og_desc'] or d['meta_desc'],
        'og_url': d['og_url'] or d['canonical'] or '',
        'og_image': d['og_image'] or '',
        'kopf_ende': kopf_ende,
        'jsonld': jsonld,
        'chrome': chrome,
        'krume': d['breadcrumb'],
        'pill': d['pill'],
        'kopfzeilen': kopfzeilen,
        'sub': d['sub'],
        'checks': checks,
        'top_kicker': d['top']['eyebrow'],
        'top_titel': hl(d['top']['titel']),
        'top_text': d['top']['text'],
        'top': top,
        'w_kicker': d['weitere']['eyebrow'],
        'w_titel': hl(d['weitere']['titel']),
        'w_text': d['weitere']['text'],
        'weitere': weitere,
        'cta_titel': hl(d['cta']['titel'], 'hl hl--center hl--klein'),
        'cta_text': d['cta']['text'],
        'cta_href': ziel_von(d['cta']['knopf']['href']),
        'cta_knopf': d['cta']['knopf']['text'],
        'fuss': fuss,
    }


def main():
    consent, kopf_ende, chrome, fuss = huelle()
    d = json.load(open(JSON, encoding='utf-8'))
    open(ZIEL, 'w', encoding='utf-8').write(bauen(d, consent, kopf_ende, chrome, fuss))
    print('geschrieben: wissen/index.html (%d Top, %d weitere)'
          % (len(d['top']['karten']), len(d['weitere']['karten'])))


if __name__ == '__main__':
    sys.exit(main())
