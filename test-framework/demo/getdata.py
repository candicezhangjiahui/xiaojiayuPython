import json
import os

with open("comparedata.json", 'r', encoding='utf-8-sig') as f:
    load_list = json.load(f) # 变成一个list
    print(load_list)
   # a = load_dict[0]["Manufacturer Part Number"] #拿里面的参数
    #print(a)
    print(load_list[0]['Manufacturer Part Number'])
    print(load_list.index)

