import qrcode

website_link = input("Provide Website Link (1 - 40): ")

version = int(input("Provide QR Code Size: "))

box_size = int(input("Provide QR Code Box Size: "))

border = int(input("Provide QR Code Border: "))

qr = qrcode.QRCode(version = version, box_size = box_size, border = border)

qr.add_data(website_link)

qr.make()

fill_color = str(input("Provide QR Code Line Color: "))

back_color = str(input("Provide QR Code Background Color: "))

img = qr.make_image(fill_color = fill_color, back_color = back_color)

img_name = input("Provide Image Name: ") + ".png"

img.save(img_name)