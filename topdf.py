import pdfkit
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

index = "learning/learning.html"
config = pdfkit.configuration(wkhtmltopdf = "wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_file(index,f"{desktop}/fb.pdf",options={"enable-local-file-access": ""},configuration=config)