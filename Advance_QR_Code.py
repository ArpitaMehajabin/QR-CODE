#nclude a logo or image in the QR code using pillow libraries
from PIL import Image
import qrcode
logo_QR = qrcode.QRCode(version=1, box_size=10, border=5)
data = "https://youtu.be/io0UQ74sXfw?si=Pkq6n1e2HYqdXoPO"
logo_QR.add_data(data)
logo_QR.make(fit=True)
img = logo_QR.make_image(fill_color = "black", backgroung_color = "white")

# Open the logo or image file
logo = Image.open("logo.PNG")

# Resize the logo or image if needed
logo = logo.resize((50,50))

# Position the logo or image in the center of the QR code
img_w, img_h = img.size
logo_w, logo_h = logo.size
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)

# Paste the logo or image onto the QR code
img.paste(logo, pos)
img.save("QR_WithLogo.png")