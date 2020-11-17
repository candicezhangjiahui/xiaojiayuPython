my_dict = {'name': 'yyh', 'age': 18, 'sex': 'male', 'hobbies': ['2', '3']}
print(my_dict['name'])
print(my_dict['hobbies'][0])
my_dict['sex'] = 'male'
my_dict['age'] = '20'
print(my_dict['age'])
print(my_dict)
print(len(my_dict))
print('key' in my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())   # 输出所有的键值对
# for 循环遍历
for key in my_dict:
    print(key)
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(key,':',value,sep='')

# get（）
print(my_dict.get('name'))
print(my_dict.get('kkk', '返回失败'))   #如果第一个指定的key值不存在，返回的就是none，第二个参数可以设置返回什么

# pop()
print(my_dict.pop('name'))
print(my_dict)

# popitem()
print(my_dict.popitem()) # 随机删除一对健值，将被删除的key和value在元组内返回
print(my_dict)

# update() //只增不减
my_dict.update({'hobbies':['reading','swimming'], 'name':'candice'})
print(my_dict)


