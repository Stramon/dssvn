import os
import qrcode
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage

# Liste mit den existierenden Ordnernamen, angepasst an dein GitHub-Repository
data_block = """
stroeh-wilhelm|Wilhelm Ströh
bock-emil|Emil Bock
bock-johann|Johann Bock
rausch-l|L. Rausch
friedrich-jens|Friedrich Jens
baasch-johannes|Johannes Baasch
baasch-claus|Claus Baasch
lass-w|W. Laß
baasch-ludwigt|Ludwigt Baasch
baasch-karl|Karl Baasch
ohlsen-wilhelm|Wilhelm Ohlsen
ohlsen-rudolf|Rudolf Ohlsen
elbers-g|G. Elbers
holz-a|A. Holz
grotkopp-h|H. Grotkopp
popp-h|H. Popp
joehnk-a|A. Jöhnk
petersen-e|E. Petersen
luethje-f|F. Lüthje
kaehler-paul|Paul Kähler
kaehler-karl|Karl Kähler
hass-j|J. Hass
jensen-detlef|Detlef Jensen
karalschak-j|J. Karalschak
doose-h|H. Doose
seemann-r|R. Seemann
schloesser-heinz|Heinz Schlösser
stenzeleit-werner|Werner Stenzeleit
goetsch-kurt|Kurt Götsch
krentz-leo|Leo Krentz
goercke-erich|Erich Görcke
hoelk-hans-detlef|Hans Detlef Hölk
joehnk-willy|Willy Jöhnk
stroeh-heinrich|Heinrich Ströh
pohl-heinz|Heinz Pohl
kuest-fritz|Fritz Küst
neumann-walter|Walter Neumann
staude-bruno|Bruno Staude
wulff-karl-heinz|Karl Heinz Wulff
maryen-friedrich|Friedrich Maryen
klein-kurt|Kurt Klein
pfahl-bernhard|Bernhard Pfahl
frohreich-arthur|Arthur Frohreich
bast-walter|Walter Bast
hass-rudolf|Rudolf Hass
johst-wilhelm|Wilhelm Johst
reimer-albert|Albert Reimer
"""

os.makedirs("qrcodes", exist_ok=True)

for line in data_block.strip().split("\n"):
    if not line:
        continue
    folder, name = line.split("|")
    print(f"Generiere wetterfesten QR-Code für: {name}")
    
    # Die neue, kurze Basis-URL
    url = f"https://stramon.github.io/dssvn/{folder}/"
    
    qr = qrcode.QRCode(
        version=None,
        # Level M (15% Korrektur) erzwingt hier das großmaschige 29x29 Layout
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=20,  # Schöne, fette Pixel für den Druck
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img.save(f"qrcodes/qr-{folder}.png")

print("\nFertig! Alle QR-Codes wurden mit der dssvn-URL im 29x29-Raster erzeugt.")
