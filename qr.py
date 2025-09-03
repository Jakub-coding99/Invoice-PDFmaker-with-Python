import qrcode


ACC_data = "CZ8606000000000213057318"
AM_data = 1000
CC_data = "CZK"
DT_data = 20250827
MSG_data = "Qr platba-test"

qr_format = f"SPD*1.0*ACC:{ACC_data}*AM:{AM_data}*CC:{CC_data}*DT:{DT_data}*MSG:{MSG_data}"


qr = qrcode.make(qr_format) 
qr.save("myqr_1.png")



