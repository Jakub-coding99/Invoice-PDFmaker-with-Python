from playwright.sync_api import sync_playwright
import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 



with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///C:/Users/PC/Desktop/faktura model/templates/index.html")
    page.pdf(path=f"{desktop}/faktura.pdf", format="A4",print_background=True)
    browser.close()