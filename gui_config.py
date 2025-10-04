import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QTableWidgetItem,QLineEdit,QTextEdit,QMessageBox, QPushButton
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
        self.table.setRowHeight(0,35)
        self.table.setFixedWidth(688)
        self.addLineButton.clicked.connect(self.add_row)
        self.user_config()
        self.table_config()
        self.config_table_cell()
        self.full_price = None
        self.full_price_byuser = None
        
    def table_config(self):
        for x in range(0,5):
            if x == 0:
                self.table.setColumnWidth(x,343)
            elif x == 3:
                self.table.setColumnWidth(x,50)    
            elif x == 4:
                self.table.setColumnWidth(x,110)

                
            else:
                self.table.setColumnWidth(x,90)
        self.table.insertRow(1)
        self.table.setSpan(1,0,1,self.table.columnCount() -1)
        self.table.verticalHeader().setVisible(False)
        
        self.item_text = QTableWidgetItem("Cena Celkem")
        self.item_text.setFlags(self.item_text.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.item_text.setFont(QFont("Arial", 10,QFont.Weight.Bold))
        self.table.setItem(1,0,self.item_text)

        
        self.sum_edit = QLineEdit("Kč")
        self.sum_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.sum_edit.setFont(QFont("Arial", 10,QFont.Weight.Bold))
        
        
        self.my_price = self.table.setCellWidget(1,self.table.columnCount()-1, self.sum_edit)
        self.table.viewport().update()

        
    def check_if_price(self):
  
        
        if self.full_price == None:
            self.full_price_byuser = self.sum_edit.text()
            

            return self.full_price_byuser
            
        else:
            return self.full_price
        
    def price_config(self):
        self.full_price = None

    def config_table_cell(self):

        rowcount = self.table.rowCount()
        for i in range(rowcount -1):
            
            widget_check = any(self.table.cellWidget(i,x) != None for x in range(self.table.columnCount()))
            if widget_check:
                continue

            line_edits = [QLineEdit() for _ in range(4)]
            
                    
            self.table.setCellWidget(i,1,line_edits[0])
            self.table.setCellWidget(i,2,line_edits[1])
            self.table.setCellWidget(i,3,line_edits[2])
            self.table.setCellWidget(i,4,line_edits[3])

            
            
            
            line_edits[3].textChanged.connect(self.get_price)
            self.sum_edit.textChanged.connect(self.price_config)
            
            text_edit = QTextEdit()
            self.table.setCellWidget(i,0,text_edit)
            text_edit.textChanged.connect(lambda row=i, te=text_edit: self.adjust_row_height(row, te))  
            
           
    def adjust_row_height(self, row, text_edit):
        doc_height = text_edit.document().size().height()
        margin = 10  
        new_height = int(doc_height) + margin
        max_height = 70
        new_height = min(new_height,max_height)
        self.table.setRowHeight(row, new_height)
            
          
    def get_price(self):
       
        total = 0
        rowcount = self.table.rowCount()
        for row in range(rowcount - 1):
            if self.table.cellWidget(row,4) is not None:
                try:
                    x = self.table.cellWidget(row,4).text()
                    total += float(x)
                except ValueError:
                    pass
        
        
        self.sum_edit.setText(f"{total:,.2f} Kč".replace(","," ").replace(".",","))
        self.full_price = self.sum_edit.text()
       
    def add_row(self):
            row_count = self.table.rowCount()
            self.table.insertRow(row_count - 1)
            self.table.setRowHeight(row_count,10)
            self.config_table_cell()
            
            
        
    
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

                elif col == 0:
                    text_input = self.table.cellWidget(row,col)
                    if text_input:
                        row_data[headers[col]] = text_input.toPlainText()
                    
                    else:
                        row_data[headers[col]] = ""
                    
                else:
                    data = self.table.cellWidget(row,col)
                    if data:
                        row_data[headers[col]] = data.text()
                
                

                    else:
                        row_data[headers[col]] = ""
                
            all_data.append(row_data)
        
        
        for data in all_data[:]:
            if all(data[key] == "" for key in headers):
                all_data.remove(data)
            
            
            if data["material_name"]:
                data["material_name"] = "<p>" + data["material_name"].replace("\n\n","</p><br><p>").replace("\n", "</p><p>")  + "</p>"
        # print(all_data)
        return all_data

    #DEFINE SUPPLIER

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
            "full_price" : self.check_if_price(),
            
            
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
        try:
            create_qr(amount=data["full_price"], invoke_num= data["others"]["invoke_num"], acc=data["others"]["bank_acc"])
        except ValueError as e:
            if str(e) == "Wrong bank account data.":
            
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error")
                msg_box.setText("Špatný formát účtu!\n"
                                "\n"
                "(předčíslí - číslo účtu / kód banky)\n" 
                "nebo\n"
                "(číslo účtu / kód banky)")
                msg_box.exec()
       
       
            elif str(e) =="Wrong price format":
                msg_box_price = QMessageBox()
                msg_box_price.setWindowTitle("Error")
                msg_box_price.setText("Zadejte celkovou cenu!")
                msg_box_price.exec()
        
            elif str(e) == "Missing currency":
                msg_box_price = QMessageBox()
                msg_box_price.setWindowTitle("Error")
                msg_box_price.setText("Chybí měna – zadejte částku včetně měny (např. 250 Kč).")
                msg_box_price.exec()
                
                


        else:
            create_pdf(data["others"]["invoke_num"])
        
        return data

   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())



