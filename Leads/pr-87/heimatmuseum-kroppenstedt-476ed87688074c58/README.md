# Heimatmuseum Kroppenstedt — statische Website

Freistehender Auftritt für das Heimatmuseum Kroppenstedt (Am Kirchhof 2–3,
39397 Kroppenstedt). Kein Framework, kein Baukasten, kein Tracker, keine externen
Aufrufe zur Laufzeit.

## Seiten

| Datei | Inhalt |
|---|---|
| `index.html` | Die Geschichte: Ankommen → die vier Leben des Hauses → drei Schaustücke → Planen → Besuchen |
| `haus.html` | Das Gebäude von 1564, der Kirchhof, die Reithufenstadt Kroppenstedt |
| `sammlung.html` | Rundgang durch die Räume, die drei Schaustücke, das Stadtarchiv im Rathaus |
| `besuch.html` | Öffnungszeiten, Termine 2026, Anfahrt, Kontakt |
| `rahmen.html` | Hülle für Stufe 3: `<title>{{TITEL}}</title>` und `<!--PFLICHT-INHALT-->` |
| `pflichtteile.json` | Recherchierte Pflichtangaben für Stufe 3, samt benannter Lücken |

Jede gebaute Seite trägt `<!--PFLICHTLINKS-->` im Fußbereich.

## Gestaltung

Das Gestaltungssystem kommt aus dem Haus, nicht aus einer Vorlage.

- **Motiv:** Die Tafel neben der Eingangstür nennt vier Jahreszahlen — 1564
  Knabenschule, 1687 Hebammenwohnung, 1833 Töchterschule, 1994 Museum. Diese vier
  Zahlen sind das durchgehende Motiv: als Leiste im Kopfbild, als Zeitspur auf der
  Startseite, als Zeile in jedem Fuß.
- **Zweites Motiv:** Die Rundbogennischen der Stadtmauer im Museumshof. Ihre Form
  ist der Rahmen der Schaustück-Bilder (`--nische`) — und sonst nirgends; alle
  anderen Kanten sind rechtwinklig wie das Fachwerk.
- **Farben:** heller Bruchstein der Börde (`--kalk`), Kalkputz (`--putz`), dunkle
  Fachwerkbalken (`--balken`), das Oxidrot der Haustafel und der Dachziegel
  (`--ziegel`), das Grün der Fensterrahmen (`--fenster`).
- **Schriften:** Fraunces (Display, variabel, mit SOFT/WONK für den handgemachten
  Zug) und Familjen Grotesk (Text). Beide OFL, lokal unter `assets/fonts/`.
- **Abstände:** eine Skala, 8/16/24/40/64/96/144 px, als `--sp-1` … `--sp-7`.
- **Bewegung:** Scroll-Reveals, sanfter Bildversatz, ein schwebender Knopf, der am
  Fuß verschwindet. Alles über `prefers-reduced-motion` abschaltbar; ohne
  JavaScript bleibt jeder Abschnitt sichtbar (die Klasse `js` setzt das Skript).

## Bauen

Die HTML-Dateien sind handgeschrieben und brauchen keinen Build. Nur die Bilder
werden erzeugt:

```
python bilder.py    # raw/*.jpg -> assets/img/*.webp + JPG-Fallback
```

`raw/` enthält die unveränderten Originale von Wikimedia Commons. Herkunft, Urheber
und Lizenz jedes Bildes stehen in `QUELLEN.md` und in `pflichtteile.json`.

## Belegpflicht

Jede Tatsache auf der Seite ist in `QUELLEN.md` einzeln belegt. Abschnitt D dort
listet, was bewusst fehlt — Trägerschaft, Eintrittspreise, Barrierefreiheit vor Ort —
und warum.
