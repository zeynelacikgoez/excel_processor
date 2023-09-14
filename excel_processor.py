import pandas as pd
import os

def process_excel_files(exports, imports, export_columns, import_columns, key_format, output_folder="xlsx"):
    # Ergebnis und Logging initialisieren
    result = {"matched_rows": 0, "errors": []}
    all_export_keys = set()
    all_filtered_data = []

    # Durchlaufen Sie alle Export-Dateien und sammeln Sie die Schlüssel
    for export_path in exports:
        try:
            export_df = pd.read_excel(f"{output_folder}/export/{export_path}", engine='openpyxl')[export_columns]
            keys = key_format.format(*[export_df[col].astype(str) for col in export_columns])
            all_export_keys.update(keys)
        except Exception as e:
            result["errors"].append(f"Error processing {export_path}: {str(e)}")

    # Durchlaufen Sie alle Import-Dateien und filtern Sie die Daten
    for import_path in imports:
        try:
            import_df = pd.read_excel(f"{output_folder}/import/{import_path}", engine='openpyxl')[import_columns]
            import_df["key"] = key_format.format(*[import_df[col].astype(str) for col in import_columns])
            
            # Filtern Sie die Daten basierend auf den Schlüsseln
            filtered_data = import_df[import_df["key"].isin(all_export_keys)].drop(columns=["key"])
            all_filtered_data.append(filtered_data)
            result["matched_rows"] += len(filtered_data)
        except Exception as e:
            result["errors"].append(f"Error processing {import_path}: {str(e)}")

    # Zusammenführen aller gefilterten Daten und Duplikate entfernen
    final_df = pd.concat(all_filtered_data, ignore_index=True).drop_duplicates()

    # Speichern Sie das endgültige DataFrame in "gefundeneWerte.xlsx"
    try:
        final_df.to_excel(os.path.join(output_folder, "gefundeneWerte.xlsx"), index=False, engine='openpyxl')
    except Exception as e:
        result["errors"].append(f"Error saving gefundeneWerte.xlsx: {str(e)}")

    return result

# Beispielaufruf der Funktion
# process_excel_files(
#     ["export1.xlsx", "export2.xlsx"],
#     ["import1.xlsx", "import2.xlsx"],
#     ["abc", "def", "ghi"],
#     ["123", "456", "789"],
#     "{}-{}-{}"
# )
