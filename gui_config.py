import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from output import Ui_MainWindow
from main import create_pdf, create_qr, render_data
import time
#pyside6-designer   

class MyApp(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.send_button.clicked.connect(self.get_data)
        self.table = self.calc_table
        self.table.setRowHeight(0,10)
        self.table.setFixedWidth(688)
        self.addLineButton.clicked.connect(self.add_row)
        self.user_config()
        self.table_config()
        
        self.get_price()
    
    def table_config(self):
        for x in range(0,5):
            if x == 0:
                self.table.setColumnWidth(x,363)
            elif x == 3:
                self.table.setColumnWidth(x,50)    
            else:
                self.table.setColumnWidth(x,90)
        self.table.insertRow(1)
        
        self.item_text = QTableWidgetItem("Cena Celkem")
        self.item_text.setFlags(self.item_text.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.item_text.setFont(QFont("Arial", 12,QFont.Weight.Bold))
        self.table.verticalHeader().setVisible(False)
        self.table.setItem(1,0,self.item_text)
        self.table.setSpan(1,0,1,self.table.columnCount() -1)

        self.item_sum = QTableWidgetItem("0 Kč")
        self.item_sum.setFont(QFont("Arial", 12,QFont.Weight.Bold))
        self.item_sum.setFlags(self.item_sum.flags() & ~Qt.ItemFlag.ItemIsEditable )
        self.table.setItem(1,self.table.columnCount()-1, self.item_sum)
        
        
        
    def get_price(self):
        total = 0
        rowcount = self.table.rowCount()
        for i in range(rowcount):
            
            if self.table.cellWidget(i,4) is not None:
                continue
            line_edit = QLineEdit()
            self.table.setCellWidget(i,4,line_edit)
            def get_text(row):
                def get(text):
                    print(text)
                    
                
                return get
            line_edit.textChanged.connect(get_text(i))
            
           
            
            
       
    def add_row(self):
            row_count = self.table.rowCount()
            self.table.insertRow(row_count - 1)
            self.table.setRowHeight(row_count,10)
            self.get_price()
            
            
    

    
    def get_table_data(self):
        all_data = []
        rows = self.table.rowCount()  - 1
        cols = self.table.columnCount()
        headers = ["material_name","amount","single_price","discount","price"]
        for row in range(rows):
            row_data = {}
            for col in range(min(cols,len(headers))):
                
                if col == 4:
                    widget = self.table.cellWidget(row,col)
                    if widget:
                        row_data[headers[col]] = widget.text()
                    else:
                        row_data[headers[col]] = ""
                else:
                    data = self.table.item(row,col)
                    if data:
                        row_data[headers[col]] = data.text()
                
                

                    else:
                        row_data[headers[col]] = ""
                
            all_data.append(row_data)
        
        for data in all_data:
            if all(data[key] == "" for key in headers):
                all_data.remove(data)
            
        return all_data

    
    def user_config(self):
        self.supplier_name.setText("Jakub Jurajda")
        self.supplier_address.setText("Prostřední Bečva 482")
        self.supplier_town.setText("Prostřední Bečva")
        self.supplier_PN.setText("756 56")
        self.supplier_ICO.setText("06929141")
    
    
    def get_data(self):
        
        data = {
            "supplier" :

                 {
                "name" : self.supplier_name.text(),
                "address" : self.supplier_address.text(),
                "town" : self.supplier_town.text(),
                "psc" : self.supplier_PN.text(),
                "ico" : self.supplier_ICO.text(),
                "dic" : self.supplier_DIC.text(),
                
                },
            
            "customer" : 
                {"name" : self.customer_name.text(),
                "address" : self.customer_address.text(),
                "town" : self.customer_town.text(),
                "psc" : self.customer_PN.text(),
                "ico" : self.customer_ICO.text(),
                "dic" : self.customer_DIC.text(),  
                },

            "calculation" : self.get_table_data(),
            
            
            "others" :

                {
                "invoke_num" : self.num_Invoke.text(),
                "issue_date" : self.issue_date.text(),
                "bank_acc" : self.bank_acc.text(),
                "due_date" : self.due_date.text(),
                "payment_method" : self.payment_method.text(),
                }
            

        }
        render_data(data)
        # create_qr(amount=500, invoke_num= data["others"]["invoke_num"])
        time.sleep(1)
        create_pdf(data["customer"]["name"])
        
        return data

    def price(self):
        row_count = self.table.rowCount()
        for row in range(row_count -1):
            print(self.table.cellWidget(row,4))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())



