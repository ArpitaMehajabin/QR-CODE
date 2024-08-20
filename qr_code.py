import qrcode
#simple QR code
# Generate_QR = qrcode.make("Let's create a QR code")
# Generate_QR.save("image.png")

# Create a QR code object with a larger size and higher error correction
QR = qrcode.QRCode(version=3, box_size= 20, border=10)
# Add the data to the QR code object 
QR.add_data("https://youtu.be/io0UQ74sXfw?si=Pkq6n1e2HYqdXoPO")
# Make the QR code
QR.make(fit = True)
# Create an image from the QR code with a black fill color and white background
img = QR.make_image(fill_color = "black", back_color = "white")
# Save the QR code image
img.save("QRCode.png")


