#!/usr/bin/env python3
"""Setzt die Domain der Seite an allen Stellen und erzeugt robots.txt, sitemap.xml, llms.txt.

    python3 tools/set_domain.py https://nutrition.rehab-five.com

Die Domain steckt in canonical, og:url, twitter:url und in mehreren JSON-LD-@ids —
verteilt ueber index.html und 22 Dateien unter wissen/. Von Hand wird das unweigerlich
inkonsistent, und eine canonical, die auf eine andere Domain zeigt als die, unter der
die Seite erreichbar ist, nimmt der Seite die Indexierung.
"""
import os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALT = "rehab-five-nutrition-ernaehrungsberatung.com"


def hole_alte_basis(text):
    m = re.search(r'https?://([a-z0-9.\-]+)/?"[^>]*rel="canonical"', text)
    m = m or re.search(r'<link rel="canonical" href="https?://([a-z0-9.\-]+)', text)
    return m.group(1) if m else ALT


def dateien():
    yield os.path.join(ROOT, "index.html")
    for name in ("impressum.html", "datenschutz.html"):
        p = os.path.join(ROOT, name)
        if os.path.exists(p):
            yield p
    w = os.path.join(ROOT, "wissen")
    for f in sorted(os.listdir(w)):
        if f.endswith(".html"):
            yield os.path.join(w, f)


def seiten_urls(basis):
    urls = [(basis + "/", "1.0"), (basis + "/wissen/", "0.8")]
    w = os.path.join(ROOT, "wissen")
    for f in sorted(os.listdir(w)):
        if f.endswith(".html") and f != "index.html":
            urls.append((basis + "/wissen/" + f, "0.7"))
    return urls


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    basis = sys.argv[1].rstrip("/")
    host = re.sub(r"^https?://", "", basis)

    alt_host = hole_alte_basis(open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
    geaendert = frei = 0
    for p in dateien():
        s = open(p, encoding="utf-8").read()
        neu = s.replace(alt_host, host).replace(ALT, host)
        # Mit der Domain faellt auch die Indexier-Sperre der Vorschau.
        if "noindex" in neu:
            neu = re.sub(
                r'<!-- Vorschau:.*?-->\n<meta name="robots" content="noindex, nofollow" />',
                '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />',
                neu, flags=re.S)
            neu = neu.replace('<meta name="robots" content="noindex, nofollow" />',
                              '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />')
            frei += 1
        if neu != s:
            open(p, "w", encoding="utf-8").write(neu)
            geaendert += 1
    print(f"{alt_host} -> {host} in {geaendert} Dateien; Indexierung freigegeben in {frei}")

    heute = datetime.date.today().isoformat()
    urls = seiten_urls(basis)
    eintraege = "\n".join(
        f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{heute}</lastmod>\n"
        f"    <priority>{prio}</priority>\n  </url>" for u, prio in urls)
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{eintraege}\n</urlset>\n")

    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\n"
        "Allow: /\n\n"
        "# Wir wollen in KI-Antworten als Quelle auftauchen, also duerfen diese Crawler lesen.\n"
        "User-agent: GPTBot\nAllow: /\n\n"
        "User-agent: OAI-SearchBot\nAllow: /\n\n"
        "User-agent: PerplexityBot\nAllow: /\n\n"
        "User-agent: ClaudeBot\nAllow: /\n\n"
        f"Sitemap: {basis}/sitemap.xml\n")

    zeilen = []
    w = os.path.join(ROOT, "wissen")
    for f in sorted(os.listdir(w)):
        if f.endswith(".html") and f != "index.html":
            s = open(os.path.join(w, f), encoding="utf-8").read()
            m = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
            t = re.search(r"<title>(.*?)</title>", s, re.S)
            titel = t.group(1).split("|")[0].split("·")[0].strip() if t else f
            zeilen.append(f"- [{titel}]({basis}/wissen/{f}): {m.group(1) if m else ''}")

    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write(
        "# REHAB FIVE NUTRITION — Ernährungstherapie Münster\n\n"
        "> Ernährungsberatung und ärztlich verordnete Ernährungstherapie in Münster, "
        "Weseler Straße 71. Teil der Physiotherapie-Praxis REHAB FIVE. Bei vielen "
        "Indikationen übernimmt die gesetzliche Krankenkasse nach §43 SGB V 80 Prozent "
        "der Kosten, einzelne Kassen bis zu 100 Prozent.\n\n"
        "Beratung nach den Leitlinien der DGE, durchgeführt von Oecotrophologinnen. "
        "Erstgespräch 60 bis 90 Minuten, ab 95 Euro. Präventionskurs nach §20 SGB V "
        "(ZPP-zertifiziert) 149 Euro, bis zu 100 Prozent erstattungsfähig.\n\n"
        f"## Seiten\n\n- [Startseite]({basis}/): Programme, Preise, Ablauf, Standort\n"
        f"- [Wissensbereich]({basis}/wissen/): 21 Fachartikel zu Indikationen\n\n"
        "## Fachartikel nach Indikation\n\n" + "\n".join(zeilen) + "\n")

    print(f"sitemap.xml ({len(urls)} URLs), robots.txt, llms.txt geschrieben")


if __name__ == "__main__":
    main()
