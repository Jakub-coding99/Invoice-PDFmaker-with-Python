x = {'supplier': {'name': 'Jakub Jurajda', 'address': 'Prostřední Bečva 482', 'town': 'Prostřední Bečva', 'psc': '756 56', 'ico': '06929141', 'dic': ''}, 'customer': {'name': 'večeřa', 'address': 'jkjk', 'town': 'jkjkjkll', 'psc': '4646', 'ico': '12121', 'dic': '21212'}, 'calculation': {'calculation': [{'material_name': 'štuk', 'amount': '200', 'single_price': '200', 'discount': '', 'price': '40000'}, {'material_name': 'fasada', 'amount': '100', 'single_price': '50', 'discount': '', 'price': '966000'}]}, 'others': {'invoke_num': '', 'issue_date': '155151', 'bank_acc': '2130571/555', 'due_date': '51515', 'payment_method': 'Převodem'}}
supp = x['supplier']["name"]
cus = x["customer"]
calc = x['calculation']["calculation"]
for row in calc:
    print(row["material_name"])