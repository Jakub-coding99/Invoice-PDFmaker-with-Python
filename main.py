import qrcode
from playwright.sync_api import sync_playwright
import os
from jinja2 import Environment, FileSystemLoader
import base64
# num_kuba = "115-7073590277/0100"
# num = "213057318/0600"

def render_data(data):
    env = Environment(loader = FileSystemLoader('templates'))

    template = env.get_template('index.html')


    with open("templates/new_model.html","w",encoding="utf-8") as file:
        
        new_file = template.render(data = data)
        file.write(new_file)
        

def create_pdf(invoke_num):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    with sync_playwright() as p:
        if "/" in invoke_num:
            formatted_invoke_num = invoke_num.replace("/","-")
            invoke_num = formatted_invoke_num
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///C:/Users/PC/Desktop/faktura model/templates/new_model.html")
        page.pdf(path=f"{desktop}/faktury/faktura-{invoke_num}.pdf", format="A4",print_background=True)
        browser.close()


def create_qr(invoke_num, amount,acc):
    from schwifty import IBAN
    import re
    bank_codes = ["3030", "2230", "2600", "0800", "7960", "0300", "6100", "2210", "2010", "0600", "2100", "3500", "5800", "0100", "4000",
                   "6210", "7990", "8040", "0300", "7950", "5500", "8030", "6800", "8060", "2700", "7980", "7970", "2310"]

    # bban = kod_banky+predcisli+cislo_uctu 
    bban = ""
    a = re.split(r"[/|-]",acc)
    
    if len(a) == 3:
        prefix = a[0].rjust(6,"0")
        acc_number = a[1].rjust(10,"0")
        bank_code = a[2]
        if bank_code not in bank_codes:
             raise ValueError("Wrong bank account data.")

       
    elif len(a) == 2:
        prefix = "000000"
        acc_number = a[0].rjust(10,"0")
        bank_code = a[1]
        if bank_code not in bank_codes:
             raise ValueError("Wrong bank account data.")
    
    else:
        
        raise ValueError("Wrong bank account data.")
    
    bban = bank_code + prefix + acc_number
        
    iban = IBAN.from_bban("CZ", bban)
    if amount:
        x = float(amount.replace("Kč","").replace(",",".").replace(" ", "").strip())
        amount_formatted = f"{x:.2f}"
    else:
        raise ValueError("Wrong price format")
    
    ACC_data = iban
    AM_data = amount_formatted
    CC_data = "CZK"
    MSG_data = f"faktura č. {invoke_num}"

    qr_format = f"SPD*1.0*ACC:{ACC_data}*AM:{AM_data}*CC:{CC_data}*MSG:{MSG_data}"


    qr = qrcode.make(qr_format) 
    qr.save("static/img/myqr.png")


