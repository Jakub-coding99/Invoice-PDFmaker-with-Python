import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from output import Ui_MainWindow

#pyside6-designer   

class MyApp(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.send_button.clicked.connect(self.get_data)


    
    def get_data(self):
        data = {
            "customer" : 
                {"name" : self.customer_name.text(),
                "address" : self.customer_address.text(),
                "town" : self.customer_town.text(),
                "psc" : self.customer_PN.text(),
                "ico" : self.customer_ICO.text(),
                "dic" : self.customer_DIC.text(),

                    
                },

            "supplier" :

                 {
                "name" : self.supplier_name.text(),
                "address" : self.supplier_address.text(),
                "town" : self.supplier_town.text(),
                "psc" : self.supplier_PN.text(),
                "ico" : self.supplier_ICO.text(),
                "dic" : self.supplier_DIC.text(),
                
                },

            # "calculation" :
            #     {"calculation" : self.calc_table.},
            
            
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

    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())