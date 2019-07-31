'''import csv 
class Stock:
    def __init__(self, name,symbol,exchange,price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price
def __str__(self):
    return f"{self.name},{self.symbol},{self.exchange},{self.price}"

try:
    with open("stock_price") as f:
        data = csv.reader("stock_price.csv") ''''

import csv
'''def hello(name,message):
    print(f"{name},{message}")

hello('hi','how are you?')
hello("message":"how are you?",name="joy")
hello(**@staticmethod
def funcname(parameter_list):
    pass)'''
class Stock:
    def __init__(self,name,symbol,exchange,price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price
    def __str__(self):
        return f"{self.name},{self.symbol},{self.exchange},{self.price}"

try:
    with open("stock_price.csv") as f:
        data = csv.reader(f,delimiter=",")
        stock_lst = []
        line =0
        for d in data:
            if line === 0:
                line +=1
                continue
            stock_lst.append(Stock(*d))
    for s in stock_lst:
        if "K" in s.price:
            s.price = float(s.price().strip().replace("K",""))*1000
        else:
            s.price = float(s.price.strip())
        print(s)

except Exception as e:
    print(e)
def show_stock_by_price(price):
    stock_lst = clean_init_get_stocks()
    f = 