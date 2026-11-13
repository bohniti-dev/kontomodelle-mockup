# Kontomodelle Kommerz Neu – Mock-up

Klickbares Mock-up einer internen Anwendung, mit der das Projekt **Kontomodelle Kommerz Neu**
(Erste Bank Österreich) definiert wird: vier neue Kontomodelle (3 + 1), der Business Case dahinter
und ein Konfigurator für Szenarien. Stand 13.11.2026, Entwurf.

> **Alle Zahlen sind Beispieldaten.** Modellnamen, Preise, Margen, Kundenzahlen und Quellen
> sind erfunden, damit der Rechenweg schlüssig ist. Die echten Werte kommen später aus dem
> Konfigurator.

Live-Version mit Interaktion: Design-Canvas unter
<https://claude.ai/artifact/ArvLDRSckTzcJJvjeA354C> (Zugriff muss vom Eigentümer freigegeben
werden). Dort ist der Konfigurator im Play-Modus bedienbar.

## Ansehen

Ohne Build: `html/Main.html` im Browser öffnen. Die Seiten sind untereinander verlinkt.

| Datei | Reiter | Inhalt |
|---|---|---|
| `html/Main.html` | Startseite | Die vier Modelle als Karten, Legende, Entstehung in fünf Schritten, Wirkung im Szenario |
| `html/BusinessCase.html` | Business Case · Gesamt | Dokument nach Standardgliederung (siehe unten) mit Inhaltsverzeichnis und Quellenverzeichnis |
| `html/BusinessCaseModell.html` | Business Case · Modell | Derselbe Rechenweg für ein einzelnes Modell, ausgearbeitet für „Kommerz Klassik“ |
| `html/Konfigurator.html` | Konfigurator | Platzhalter: die interaktive Seite läuft nur im Canvas, Verhalten steht unten |
| `html/Feldzustaende.html` | Komponente | Ein Business-Case-Feld in seinen drei Zuständen |

`design/project/` enthält die Originalquellen des Canvas (`*.dc.html`, `canvas.json`).
Sie brauchen die Canvas-Laufzeit; `tools/standalone.py` erzeugt daraus die Dateien in `html/`.

## Die vier Modelle (3 + 1)

| Modell | Zielgruppe | Preis / Monat | Herkunft |
|---|---|---|---|
| Kommerz Start | Wenignutzer, ≤ 30 Buchungen | 9,90 € | Cluster „Wenig“ |
| Kommerz Klassik | Regelnutzer, 31–150 Buchungen | 19,90 € | Cluster „Regel“ (größtes Segment) |
| Kommerz Premium | Vielnutzer, fester Betreuer | 39,90 € | Cluster „Viel“ |
| Kommerz Digital (+1) | reine Online-Kunden | 4,90 € | Cluster „Nur online“, Antwort auf Neobanken |

Preis = Kostenbasis ÷ (1 − Zielmarge), geprüft am Marktmedian, gerundet auf x,90.

## Struktur des Business Case

Der Reiter folgt dem Standardaufbau eines Business Case
([Wikipedia](https://en.wikipedia.org/wiki/Business_case)):

0. Vorwort · 1. Executive Briefing (Empfehlung, Ergebnisse, Entscheidung) · 2. Einleitung
(Treiber, Umfang, Finanzkennzahlen) · 3. Analyse (Annahmen, Cashflow und Barwert, Kosten,
Nutzen, Risiken, Umsetzungsplan, strategische Optionen, Opportunitätskosten) · 4. Schluss und
nächste Schritte · 5. Anhang (A Rechenweg in fünf Schritten, B Quellenverzeichnis).

Quellenverweise im Text sind kleine blaue Nummern `[3]` und springen zum Eintrag im
Quellenverzeichnis. Das Verzeichnis entsteht aus den Confluence-Links der verifizierten Felder.

## Visuelle Sprache (auf allen Seiten gleich)

| Darstellung | Bedeutung |
|---|---|
| Weißer Rahmen, blauer Haken | **Eingabe, verifiziert**: Wert mit Confluence-Quelle. Der Haken ist der Link. |
| Weißer Rahmen, oranges „A“ | **Eingabe, Annahme**: Schätzung des Teams ohne Beleg |
| Grau gestrichelt, Kästchen „=“ | **Berechnet**: wird nie eingegeben, folgt aus Eingaben; Formel meist daneben |
| Orange | heute / Risiko / Annahme |
| Blau | neu / verifiziert / Empfehlung |

Farben: Grund `#F4F6F9`, Text `#0F172A`, Akzent `#1A56DB`, Annahme `#9A3412` auf `#FEF0E6`,
Verifiziert-Chip `#153FA3` auf `#E8F0FE`, Heute/Risiko in Diagrammen `#C2410C`. Schrift Inter.
Es ist bewusst **kein** Erste-Bank-Branding; die CI kommt später über die Farbvariablen.

## Datenmodell eines Business-Case-Felds

```
Feld
  key        Variablenname, z. B. kosten_buchung (für Formeln)
  name       Anzeigename
  value      Freitext: Zahl ("12,40"), Text oder Formel ("= kosten_buchung × 150")
  unit       Einheit
  status     "annahme" | "verifiziert"
  link       Confluence-URL, Pflicht bei "verifiziert"
  owner      verantwortliche Person oder Einheit
  slider     optional { min, max, step } – nur für Annahmen, bei denen kein Beleg zu erwarten ist
  group      Bestand & Kosten | Segmentierung | Marge & Preis | Markt & Migration
```

Regeln:

- Ein Feld gilt nur dann als verifiziert, wenn `status = verifiziert` **und** ein gültiger
  Confluence-Link (`https://…`) hinterlegt ist. Ohne Link: Haken grau gestrichelt, Hinweis
  „Confluence-Link erforderlich“, das Feld zählt weiter als Annahme.
- Der blaue Haken erscheint überall, wo der Wert auftaucht, und öffnet die Quelle in einem neuen Tab.
- Verifizierte Felder bekommen eine fortlaufende Nummer im Quellenverzeichnis.
- Belastbarkeit = verifizierte Felder ÷ alle Felder (im Mock-up 14 / 22 = 64 %).
- Formeln (Wert beginnt mit `=`) rechnen im Business Case live mit.

## Konfigurator (Verhalten)

- **Szenarien** links: auswählen, „Als Kopie speichern“, „Neues Szenario“, „Szenario speichern“.
  Jedes Szenario hält einen vollständigen Satz Eingaben.
- **Eingaben** gruppiert in vier Gruppen; je Zeile Variable, Wert, Einheit, Status-Umschalter
  (Annahme | Verifiziert), Quelle.
- **Schieberegler**: Felder mit `slider` zeigen im Status Annahme einen Regler mit Spanne statt
  des Textfelds; beim Umschalten auf Verifiziert wird daraus ein Textfeld plus Link-Feld.
  Im Mock-up: Beratungsstunde 50–120 €, Beratung je Klassik-Kunde 0–0,1 h, Schwelle Vielnutzer
  80–250, Zielmarge Premium 20–45 %, Abwanderung 0–15 %, Rückgewinn Digital 0–6.000 Kunden.
- **Filter**: Alle · Annahmen · Verifiziert · Mit Schieberegler.
- **„Daraus berechnet“** unter jeder Gruppe zeigt die abhängigen Werte und reagiert sofort
  (im Mock-up: Kostenbasis und rechnerischer Preis Klassik, Preis Premium, Abwanderungsrisiko,
  Ertragsdelta).
- Seitenleiste „Wirkung dieses Szenarios“: Ertragsdelta, Kunden teurer, Abwanderungsrisiko,
  Belastbarkeit mit Balken.

## Rechenweg (Beispielwerte)

1. **Ist-Analyse**: Kunden, Ø Ertrag, Kosten je Buchung/Karte/Beratungsstunde →
   Ertrag heute, Kostenbasis je Modell.
2. **Segmentierung**: Schwellen 30 / 150 Buchungen, Kanalnutzung → Cluster 31 / 44 / 12 / 13 %.
3. **Modellbildung**: je Cluster ein Leistungsbündel → Start, Klassik, Premium, Digital.
4. **Preisbildung**: Kostenbasis ÷ (1 − Marge), Marktmedian, Rundung → 9,90 / 19,90 / 39,90 / 4,90 €.
5. **Marktwirkung**: Migrationsregel, Abwanderung bei Verteuerung, Rückgewinn Digital →
   Ertrag neu, Abwanderungsrisiko, Delta.

Beispiel Klassik: 85 × 0,11 € + 2 × 0,60 € + 0,022 h × 84 € = 12,40 €;
12,40 ÷ (1 − 0,38) = 20,00 €; Markt 20,70 €; Vorschlag 19,90 €.

## Offene Punkte

- Modellsichten für Start, Premium und Digital: im Mock-up nur Klassik ausgearbeitet.
- Wo und wie Szenarien gespeichert werden (Nutzer, Versionen, Vergleich zweier Szenarien).
- Confluence-Anbindung: Link nur prüfen oder Seitentitel und Stand automatisch holen?
- Echte Datenquellen für die verifizierten Felder; Kalkulationszins; IT-Einmalkosten.
