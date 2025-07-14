# Last Resort Getränkekarten-Generator

Dieses Projekt erzeugt automatisch eine zweispaltige PDF-Getränkekarte im Stil von „Last Resort“ auf Basis einer JSON-Datei und einer LaTeX-Vorlage.

## 📦 Inhalt

```bash
.
├── drinks_full.json           # Vollständige Getränkedatenbank (Cocktails, Shots etc.)
├── last_resort_template.tex   # LaTeX-Vorlage mit Platzhalter {content}
├── last_resort_generated.tex  # Automatisch erstellte LaTeX-Datei (kompilierbar)
└── generate_menu.py           # (optional) Python-Skript zum Generieren der Karte
```

---

### 3. Voraussetzungen
```markdown
## 🛠 Voraussetzungen

- Python 3.x
- LaTeX mit `pdflatex` (z. B. TeX Live, MikTeX)
- Optional: `logo.png` im Ordner `images/` für das Branding

## 🧪 Beispielausführung

```bash
python generate_menu.py
pdflatex last_resort_generated.tex
```

---

### 5. JSON-Datenstruktur
```markdown
## 🧾 JSON-Datenstruktur

Die `drinks_full.json` Datei enthält Kategorien wie `cocktails`, `softdrinks`, `shots` usw. – jede mit:

```json
{
  "name": "Gin Basil Smash",
  "price": "10,-",
  "ingredients": "Gin, Basilikum, Limette"
}
```

---

### 6. Layoutbeschreibung
```markdown
## 🎨 Layout

- **Zweispaltig**: linke Spalte Cocktails & Specials, rechte Spalte alkoholfreie Getränke, Shots & Bier
- **Logo**: optional zentriert oben (`images/logo.png`)
- **Fußnote**: „Alle Preise inkl. MwSt. +1 € RECUP Pfand“

## 📄 PDF-Erzeugung

Um das fertige PDF zu erhalten:

1. Daten in `drinks_full.json` anpassen
2. `generate_menu.py` ausführen (optional)
3. LaTeX kompilieren:

```bash
pdflatex last_resort_generated.tex
```


---

### 8. Vorschau (optional)
```markdown
## ✅ Beispiel

[📄 Vorschau ansehen](images/last_resort_generated.pdf)

---

### Lizenz

MIT License – Feel free to fork, use, adapt.
