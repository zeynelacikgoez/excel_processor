
# Excel Data Processing Library

Diese Bibliothek bietet verschiedene Funktionen zur Datenverarbeitung in Excel. Sie wurde entwickelt, um den Umgang mit Excel-Dateien in Python zu erleichtern, insbesondere im Hinblick auf das Mergen, Filtern und Verarbeiten von Daten aus mehreren Dateien.

## Hauptmerkmale

- **Vergleich von Daten aus mehreren Excel-Dateien**: Mit der Funktion `process_excel_files` können Sie Daten aus mehreren Export- und Import-Dateien vergleichen und die Ergebnisse in einer einzigen Datei speichern.
- **Erweiterte Fehlerbehandlung**: Die Bibliothek bietet robuste Fehlerbehandlung und Logging, um Sie über eventuelle Probleme oder Unstimmigkeiten in den Daten zu informieren.
- **Flexibilität**: Flexibilität bei der Angabe von Spaltennamen, Schlüsselformaten und Dateipfaden.
- **(Weitere Funktionen)**: Da diese Bibliothek ständig erweitert wird, werden hier in Zukunft weitere Datenverarbeitungsfunktionen hinzugefügt.

## Installation

Um diese Bibliothek zu verwenden, klonen Sie einfach das Repository:

```
git clone https://github.com/zeynelacikgoez/excel_processor.git
```

Stellen Sie sicher, dass Sie `pandas` und `openpyxl` installiert haben:

```
pip install pandas openpyxl
```

## Verwendung

### process_excel_files

Ein Beispielaufruf der Funktion `process_excel_files`:

```python
from excel_processor import process_excel_files

result = process_excel_files(
    ["export1.xlsx", "export2.xlsx"],
    ["import1.xlsx", "import2.xlsx"],
    ["abc", "def", "ghi"],
    ["123", "456", "789"],
    "{}-{}-{}"
)
print(result)
```
