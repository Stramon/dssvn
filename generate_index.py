import os

# Konfiguration
target_file = "index.md"
ignored_folders = {".git", ".venv", "qrcodes", "import_text", "__pycache__", "Bilder", "_includes"}

# Marker für den dynamischen Bereich
start_marker = "<!-- SOLDIER_LIST_START -->"
end_marker = "<!-- SOLDIER_LIST_END -->"

# 1. Existierenden Text einlesen und Text deiner Mutter schützen
header_text = ""
footer_text = ""

if os.path.exists(target_file):
    with open(target_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    if start_marker in content and end_marker in content:
        # Perfekt: Marker existieren bereits. Wir isolieren Kopf und Fuß.
        header_text = content.split(start_marker)[0].strip() + "\n\n" + start_marker + "\n"
        footer_text = "\n" + end_marker + "\n" + content.split(end_marker)[1].strip() + "\n"
    else:
        # Erster Durchlauf: Wir trennen den Text vor dem ersten Bullet-Point
        lines = content.splitlines()
        header_lines = []
        for line in lines:
            if line.strip().startswith("*"):
                break
            header_lines.append(line)
        
        header_text = "\n".join(header_lines).strip() + "\n\n" + start_marker + "\n"
        footer_text = "\n" + end_marker + "\n"
else:
    # Absoluter Notfall-Fallback, falls die Datei komplett fehlen sollte
    header_text = f"""# Die sprechenden Steine von Neuwittenbek
### 150 Jahre Dorfjubiläum • Gedenkprojekt

Scannen Sie die QR-Codes an den Gedenksteinen, um mehr über das Leben und Schicksal der unserer getöteten Nachbarn, Väter, Brüder und Söhne und Ehemänner zu erfahren. Nachfolgend finden Sie die Gesamtübersicht:

{start_marker}
"""
    footer_text = f"\n{end_marker}\n"

print("Lese bestehende index.md ein und schütze manuelle Texte...")

# 2. Alle Verzeichnisse auflisten und sortieren
folders = sorted(os.listdir("."))
markdown_links = []

for folder in folders:
    if os.path.isdir(folder) and folder not in ignored_folders:
        parts = folder.split("-")
        if len(parts) >= 2:
            nachname = parts[0].capitalize()
            vorname_parts = [p.capitalize() for p in parts[1:]]
            vorname = " ".join(vorname_parts)
            
            if len(vorname) == 1:
                vorname += "."
                
            display_name = f"{vorname} {nachname}"
        else:
            display_name = folder.capitalize()
            
        markdown_links.append(f"* [{display_name}](./{folder}/)")

# 3. Datei sauber zusammenbauen und schreiben
with open(target_file, "w", encoding="utf-8") as f:
    f.write(header_text)
    f.write("\n".join(markdown_links))
    f.write(footer_text)

print(f"✓ {target_file} wurde erfolgreich aktualisiert! Die Liste umfasst jetzt {len(markdown_links)} Einträge.")
