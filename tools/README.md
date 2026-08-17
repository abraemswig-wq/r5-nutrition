# Wissen — Inhalt, Generator, Pruefung

Der Bereich `wissen/` besteht aus einer Uebersicht und 21 Fachartikeln zu
Indikationen. Beides wird erzeugt, nicht von Hand gepflegt.

## Eine Wahrheit

Bis August 2026 lagen zwei Quellen nebeneinander: ein Generator, der nur 14 der
21 Artikel kannte, und sieben Artikel, die es ausschliesslich als HTML gab. Jede
Reparatur an einer Seite hielt bis zum naechsten Generatorlauf. Seitdem gilt:

- **Text** steht in `wissen_inhalt.json` (21 Artikel) und `wissen_index.json`
  (Uebersicht). Inhaltliche Aenderungen passieren dort.
- **Design** steht im uebrigen Seitenbestand. Die Generatoren schneiden Consent,
  Kopfleiste, Menue und Fuss aus `programme.html` heraus; wer die Navigation
  aendert, aendert sie einmal.

Der alte `build_wissen_articles.py` ist entfernt. Er haette die Seiten mit
Tailwind-Markup ueberschrieben (siehe Git-Historie, falls jemand nachlesen will).

## Ablauf

```bash
cd /Users/aricbramswig/Downloads/rehab-five-nutrition
python3 tools/build_wissen.py         # 21 Artikel
python3 tools/build_wissen_index.py   # wissen/index.html
python3 tools/wissen_pruefen.py       # muss 0 melden
```

`wissen_extract.py` war die einmalige Archaeologie: es hat den Inhalt aus den
alten Tailwind-Seiten in die JSON gezogen. Es liest Markup, das es nicht mehr
gibt, und laeuft heute nur noch gegen ein Backup der alten Seiten.

## Was die Pruefung leistet

`wissen_pruefen.py` vergleicht jeden sichtbaren Textknoten der gebauten Seiten
gegen die JSON und meldet zwei Klassen von Fehlern:

1. **Text, der auf der Seite steht, aber nicht in der JSON** — dann hat der
   Generator etwas erfunden oder eine Aenderung wurde am Ergebnis statt an der
   Quelle gemacht.
2. **Unausgeglichene div-Klammern** im Artikeltext. Das kostet keinen Buchstaben
   und faellt der Textpruefung nicht auf, schliesst aber das Layoutraster zu
   frueh: die Randspalte mit Verzeichnis und Terminkarte rutscht aus dem Artikel
   heraus. Genau das ist einmal passiert, in allen 21 Artikeln gleichzeitig.

Zwei Fallen, die beim Bauen Zeit gekostet haben und in den Skripten
dokumentiert sind:

- Tags mit `<[^>]+>` zu entfernen verschluckt bei einem `<` im Fliesstext
  ("Natrium < 2,3 g") ganze Absaetze — und versteckt echten Inhalt als
  vermeintlichen Verlust. Deshalb ueberall `</?[a-zA-Z][^<>]*>`.
- Ausgestanzte Ueberschriften (`.hl__line`) brechen nicht um (`white-space:pre`).
  Der Generator teilt sie vorher an Wortgrenzen; siehe `ZEILE_MAX`.

## Was bewusst so bleibt

- **Die Aufteilung 7 / 14 auf der Uebersicht** ist redaktionell: sieben
  Indikationen mit voller Tiefe, vierzehn als Kurzfassung. Zusammenziehen wuerde
  bei allen 21 dieselbe Tiefe versprechen.
- **`noindex, nofollow`** auf allen 22 Seiten. Solange die Domain nicht
  entschieden ist, darf Google den Bereich nicht indexieren. Zurueckgesetzt wird
  das von `set_domain.py`, nicht von Hand.
- **Kein Autorenname.** `set_autorin.py --setzen` erst, wenn die Artikel
  fachlich freigegeben sind.
- **Kein Aufmacherbild.** Fuer 21 Indikationen gibt es kein ehrliches
  Bildmaterial; ein Symbolbild pro Krankheitsbild waere Dekoration ohne Aussage.

## Offen

- `robots.txt` und `sitemap.xml` fehlen.
- Die FAQ-Fragen im JSON-LD und in den `<details>` decken sich nicht ueberall.
- Die meta-description der Uebersicht ist 170 Zeichen lang (Korridor 70–160).
