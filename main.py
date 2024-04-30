from PIL import Image, ImageDraw, ImageFont

# Dimensioni dell'immagine
width = 400
height = 200

# Crea un'immagine con uno sfondo bianco
image = Image.new("RGB", (width, height), "white")

# Carica un font personalizzato (assicurati di sostituire 'path_al_font' con il percorso del tuo file font)
font = ImageFont.truetype("path_al_font", 36)

# Crea un oggetto ImageDraw per disegnare sull'immagine
draw = ImageDraw.Draw(image)

# Testo da scrivere
text = "Benvenuti"

# Dimensioni del testo
text_width, text_height = draw.textsize(text, font=font)

# Posizione del testo centrato sull'immagine
x = (width - text_width) / 2
y = (height - text_height) / 2

# Colore del testo
text_color = "black"

# Disegna il testo sull'immagine
draw.text((x, y), text, fill=text_color, font=font)

# Salva l'immagine
image.save("benvenuti.png")

