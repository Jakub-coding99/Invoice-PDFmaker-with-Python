## 📝 Popis (ČEŠTINA)

# Invoice Generator

![Image](https://github.com/user-attachments/assets/0f62662d-913a-4210-b1f1-526867c0a06e)



Desktopová aplikace pro generování faktur.

Tato aplikace umožňuje uživateli snadno zadat data faktury přes grafické uživatelské rozhraní vytvořené pomocí **PyQt6 + PySide6**.  

Data se následně vloží do stylované HTML šablony pomocí **Jinja2**, která vytvoří  fakturu ve formátu HTML, které se následně vygeneruje v PDF pomocí **Playwright**. Součástí  faktury je také automaticky vytvořený **QR kód** pro platbu.

## ⚙️ Použité technologie

- **PySide6 / PyQt6** – pro tvorbu grafického uživatelského rozhraní (GUI)
- **Jinja2** – pro zpracování a vyplnění HTML šablony daty
- **qrcode**  – generování QR kódů
- **Playwright** - vytvoření PDF
- **Python 3.8+**

## ✨ Funkce

- Uživatelsky  formulář pro zadání dat faktury
- Dynamické vytváření HTML faktur na základě šablony
- Automatická tvorba QR kódu
- Export faktury do PDF 
## 🚀 Instalace

1. Klonuj repozitář
   ```bash
   git clone https://github.com/Jakub-coding99/Invoice-PDFmaker-with-Python.git
   ```

2. Spusť 
    ```bash
    pip install -r requirements.txt
    ```

3. Nainstaluj Playwright prohlížečové enginy:
    ```bash
    playwright install
    ```

4. Pro podpis přidej obrazek podpisu do static/img, ideálně s pruůhledným pozadím.

5. Spusť 
    ```bash
    gui_config.py
    ```
![Image](https://github.com/user-attachments/assets/c35c38e6-e4fc-44be-b962-7903d25b60bd) 



##  📝 Description (English)

Desktop application designed to create invoice in PDF format.

This application allows user to enter data via GUI created by **PyQt6 + PySide6**. 

Data sequentially paste to styled HTML template using **Jinja2**  which creates HTML and then generate PDF using **Playwright**. 
An automatically generated **QR** code is also included for payment.


## ⚙️ Used Technologies

- **PySide6 / PyQt6** – for GUI creation
- **Jinja2** – for HTML template creation
- **qrcode**  – QR code generation
- **Playwright** - Create PDF
- **Python 3.8+**

## ✨ Features

- User-friendly form for entering invoice data

- Dynamic HTML invoice generation from a template

- Automatic QR code generation

- Export invoice to PDF format


## 🚀 Installation

1. Clone repository
   ```bash
   git clone https://github.com/Jakub-coding99/Invoice-PDFmaker-with-Python.git
   ```
2. Run 
    ```bash
    pip install -r requirements.txt
    ```

3. Install Playwright browser engines:
    ```bash
    playwright install
    ```
   
4. For sign add image of sign to static/img. Transparent background preffered.


5. Run
    ```bash
    python gui_config.py




    ```



