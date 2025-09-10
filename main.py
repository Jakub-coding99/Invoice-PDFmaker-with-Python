import qrcode
from playwright.sync_api import sync_playwright
import os
from jinja2 import Environment, FileSystemLoader


def render_data(data):
    env = Environment(loader = FileSystemLoader('templates'))

    template = env.get_template('index.html')


    with open("templates/new_model.html","w",encoding="utf-8") as file:
        
        new_file = template.render(data = data)
        file.write(new_file)
        

def create_pdf(name):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///C:/Users/PC/Desktop/faktura model/templates/new_model.html")
        page.pdf(path=f"{desktop}/faktura-{name}.pdf", format="A4",print_background=True)
        browser.close()


def create_qr(invoke_num, amount):
    ACC_data = "CZ8606000000000213057318"
    AM_data = amount
    CC_data = "CZK"
    MSG_data = f"faktura č. {invoke_num}"

    qr_format = f"SPD*1.0*ACC:{ACC_data}*AM:{AM_data}*CC:{CC_data}*MSG:{MSG_data}"


    qr = qrcode.make(qr_format) 
    qr.save("static/img/myqr_1.png")


