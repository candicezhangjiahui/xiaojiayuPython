import json
import re
new_list = []
with open(r'comparedata.json', 'r', encoding = 'UTF-8') as f:
    datatext = f.read()
    new_data_list = re.split('},', datatext)
    #分割的时候 把}去掉了，所以后面需要再把}加到新的json对象后面，这样一个json对象才完整 {}
    for i in new_data_list:
        ii = i+'}'
        new_list.append(ii)
def serch_str_list(mpn_full):  # 查询参数有没有在对应的json对象里面，有就转成字典返回
    for i in new_list:          #find查看字符串里面有没有对应的值，没有固定返回 -1
        if i.find(mpn_full) > 0 :
            data_text_dict = json.loads(i)
            print(data_text_dict['Manufacturer Part Number'])
            return data_text_dict
        else:
            continue
serch_str_list('CRCW060310K0FKEA')