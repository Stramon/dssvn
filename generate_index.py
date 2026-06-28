import os

# Konfiguration
target_file = "index.md"
# HIER: "Bilder" wurde zur Blacklist hinzugefügt
ignored_folders = {".git", ".venv", "qrcodes", "import_text", "__pycache__", "Bilder"}

# Dein fester Einleitungstext
header_text = """# Die sprechenden Steine von Neuwittenbek
### 150 Jahre Dorfjubiläum • Gedenkprojekt

Scannen Sie die QR-Codes an den Gedenksteinen, um mehr über das Leben und Schicksal der gefallenen Soldaten zu erfahren. Nachfolgend finden Sie die Gesamtübersicht:

"""

print("Generiere automatische Übersichtsliste...")

# Alle Verzeichnisse auflisten und sortieren (sortiert automatisch nach Nachnamen, da der Slug mit dem Nachnamen beginnt)
folders = sorted(os.listdir("."))
markdown_links = []

for folder in folders:
    if os.path.isdir(folder) and folder not in ignored_folders:
        # Ordner-Slug in schönen Namen umwandeln (z.B. jensen-alfred -> Alfred Jensen)
        parts = folder.split("-")
        if len(parts) >= 2:
            nachname = parts[0].capitalize()
            vorname_parts = [p.capitalize() for p in parts[1:]]
            vorname = " ".join(vorname_parts)
            
            # Falls nur ein Kürzel existiert (z.B. grotkopp-h -> H. Grotkopp)
            if len(vorname) == 1:
                vorname += "."
                
            display_name = f"{vorname} {nachname}"
        else:
            display_name = folder.capitalize()
            
        # Relative Verlinkung für GitHub Pages bauen
        markdown_links.append(f"* [{display_name}](./{folder}/)")

# Datei schreiben
with open(target_file, "w", encoding="utf-8") as f:
    f.write(header_text)
    f.write("\n".join(markdown_links))
    f.write("\n")  # Abschließende Leerzeile

print(f"✓ {target_file} wurde erfolgreich mit {len(markdown_links)} Einträgen aktualisiert!")
