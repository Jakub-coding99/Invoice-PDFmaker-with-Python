import qrcode

def create_qr():
    ACC_data = "CZ8606000000000213057318"
    AM_data = 1111
    CC_data = "CZK"
    MSG_data = "Qr platba-test"

    qr_format = f"SPD*1.0*ACC:{ACC_data}*AM:{AM_data}*CC:{CC_data}*MSG:{MSG_data}"


    qr = qrcode.make(qr_format) 
    qr.save("static/img/myqr_1.png")



create_qr()