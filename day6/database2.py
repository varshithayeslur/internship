''' using csv '''
'''import csv
data_list = [
    {"id" :1001,"wname":"python", "year": "2019","status":1,"company":"TCS"},
    {"id" :1002,"wname":"Java", "year": "2020","status":1,"company":"ITC"}
]

try:
    with open ("ws.csv","w",newline='') as file:
        heading = ["id","wname","year","status","company"]
        obj = csv.DictWriter(file,fieldnames = heading)
        obj.writeheader()
        obj.writerows(data_list)
except Exception as e:
    print(str(e)) '''

'''using json'''
import json
data_list = [
    {"id" :1001,"wname":"python", "year": "2019","status":1,"company":"TCS"},
    {"id" :1002,"wname":"Java", "year": "2020","status":1,"company":"ITC"}
]
try:
    with open("ws.json","w",newline='') as file:
        json.dump(data_list,file,indent=4)
except Exception as e:
    print(str(e))      