import pyqrcode
import png
from PIL import Image
link = input("Enter anython to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png",scale=5)
Image.open("QRCODE.PNG")
#print("hello")