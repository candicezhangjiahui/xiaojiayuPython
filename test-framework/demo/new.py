#import json

#with open("comparedata.json", 'r', encoding='utf-8-sig') as f1:
 #   dict1 =json.load(f1)
#with open("cadicedata.json", 'r', encoding='utf-8-sig') as f2:
#    dict2 = json.load(f2)
#print(dict2)
#print(dict1)

import json as js
import difflib

f = open('comparedata.json', encoding='UTF-8')
m = open('cadicedata.json', encoding='UTF-8')

x = js.load(f)
y = js.load(m)

for my_key in x.keys():
    value_eval = x[str(my_key)]
    value_test = y[str(my_key)]
    diff = difflib.SequenceMatcher(None, value_eval, value_test).quick_ratio()
    print(my_key, diff)