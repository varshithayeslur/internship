'''using list'''
'''data_list = [ 
    [1001,"python",2019,1,"TCS"],
    [1002,"Java",2020,1,"ITC"],
    [1003,"IoT",2018,1,"Amazon"]
]
try:
    with open ("ws.txt","w") as file:
        for d in data_list:
            line = f'{d[0]},{d[1]},{d[2]},{d[3]},{d[4]}\n'
            file.write(line)
except Exception as e:
    print(str(e)) '''


'''' using dictionary'''
ws_list = [
    {"id" :1001,"wname":"python", "year": "2019","status":1,"company":"TCS"},
    {"id" :1002,"wname":"Java", "year": "2020","status":1,"company":"ITC"}
]
try:
    with open ("ws.txt","w") as file:
        for d in ws_list:
            line = f'{d["id"]},{d["wname"]},{d["year"]},{d["status"]},{d["company"]}\n'
            file.write(line)
except Exception as e:
    print(str(e))
