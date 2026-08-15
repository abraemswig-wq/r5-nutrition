#!/usr/bin/env python3
"""Weist Maya Pilgram als fachliche Autorin der 21 Wissensartikel aus.

    python3 tools/set_autorin.py --pruefen    zeigt nur, was sich aendern wuerde
    python3 tools/set_autorin.py --setzen     schreibt die Aenderung

ERST AUSFUEHREN, WENN MAYA DIE ARTIKEL GEGENGELESEN UND ZUGESTIMMT HAT.
Es geht um medizinnahe Inhalte. Eine Person als fachliche Autorin auszuweisen,
ohne dass sie den Text kennt, waere eine Falschaussage ihr gegenueber und
gegenueber Leserinnen und Lesern.

Warum ueberhaupt: Google bewertet bei Gesundheitsthemen, ob eine erkennbare
Fachperson hinter dem Text steht. Aktuell steht dort nur die Organisation.
Die lokalen Wettbewerber in Muenster sind teils arztgefuehrt und haben an
dieser Stelle einen Vorsprung, der sich mit einer echten Fachautorin schliessen laesst.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WISSEN = os.path.join(ROOT, "wissen")

PERSON = """{
        "@type": "Person",
        "@id": "%(basis)s/#maya-pilgram",
        "name": "Maya Pilgram",
        "jobTitle": "Ernährungsberaterin",
        "hasCredential": {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "Bachelor of Science Oecotrophologie"
        },
        "worksFor": { "@id": "https://rehab-five.com/#organization" }
      }"""

ALT = '"author": { "@id": "https://rehab-five.com/#organization" }'


def basis_url():
    s = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r'<link rel="canonical" href="(https?://[^"/]+)', s)
    return m.group(1) if m else "https://nutrition.rehab-five.com"


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("--pruefen", "--setzen"):
        sys.exit(__doc__)
    schreiben = sys.argv[1] == "--setzen"
    basis = basis_url()
    person = PERSON % {"basis": basis}

    treffer = 0
    for f in sorted(os.listdir(WISSEN)):
        if not f.endswith(".html") or f == "index.html":
            continue
        p = os.path.join(WISSEN, f)
        s = open(p, encoding="utf-8").read()
        if "maya-pilgram" in s:
            continue
        if ALT not in s:
            print(f"  uebersprungen (anderes author-Muster): {f}")
            continue
        neu = s.replace(ALT, '"author": %s' % person)
        # Sichtbare Autorenzeile neben dem Stand-Datum: Google wertet nur aus,
        # was auch fuer Leserinnen und Leser sichtbar ist.
        neu = neu.replace(
            "<span>📅 Stand: 15. Mai 2026</span>",
            "<span>📅 Stand: 15. Mai 2026</span>\n          "
            "<span>✍️ Fachlich verantwortlich: Maya Pilgram, B.Sc. Oecotrophologie</span>", 1)
        treffer += 1
        if schreiben:
            open(p, "w", encoding="utf-8").write(neu)

    print(f"{'geschrieben' if schreiben else 'wuerde aendern'}: {treffer} Artikel (Basis {basis})")
    if not schreiben:
        print("Zum Anwenden: python3 tools/set_autorin.py --setzen")


if __name__ == "__main__":
    main()
