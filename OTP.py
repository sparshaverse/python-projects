import qrcode
data = "Sparsha Dey"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("QR Code Generated Successfully!")
