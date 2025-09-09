import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from output import Ui_MainWindow

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
        for x in range(0,5):
            if x == 0:
                self.table.setColumnWidth(x,332)
            elif x == 3:
                self.table.setColumnWidth(x,60)    
            else:
                self.table.setColumnWidth(x,90)
    
    def add_row(self):
            row_count = self.table.rowCount()
            self.table.insertRow(row_count)
            self.table.setRowHeight(row_count,10)
            
        
    
    def get_table_data(self):
        all_data = []
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        headers = ["material_name","amount","single_price","discount","price"]
        for row in range(rows):
            row_data = {}
            for col in range(min(cols,len(headers))):
                data = self.table.item(row,col)
                if data:
                    row_data[headers[col]] = data.text()
                else:
                    row_data[headers[col]] = ""
            all_data.append(row_data)
        
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
        print(data)
        
        return data

    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())


# from jinja2 import Environment, FileSystemLoader

# env = Environment(loader = FileSystemLoader('templates'))

# template = env.get_template('index.html')
# dic = {
#     "name": "jakub",
#     "age" : "26",
#     "work" :
#         [
# {
#        "position" :"chemik",
#        "delka" : 7
#     },
#     {
#        "position" :"chemik",
#        "delka" : 7
#     }

#         ]
   

# }

# with open("test.html","w") as file:
    
#     new_file = template.render(dic = dic)
#     file.write(new_file)
    
