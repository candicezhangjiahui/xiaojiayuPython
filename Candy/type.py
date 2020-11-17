counter = 100
miles = 1000.0
name = 'runoob'
print(counter,miles,name)
a = b = c = 1
d, e, f = 1, 2, 'name'
print(a, b, c, d, e, f)
# number类型：int,float,bool,complex
x = 111
print(isinstance(x, int))
del x
x=1.2
print(x)
t = ['a', 'b', 'c', 'd', 'e']
print(t[1:3])
t[0] = 9
print(t)
t[2:5] = []
print(t)
# 字典
dict = {}  # 创建空字典
dict['one'] = "1-菜鸟教程"
dict[2] = "2-菜鸟工具"
tinydict = {'name':'runoob', 'code':1, 'site':"www.runoob.com"}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
dict2 = {x: x**2 for x in (2, 4, 6)}
print(dict2)
del(dict)
dict3=dict(runoob=1, google=2, taobao=3)  #构造函数dict（）可以直接从键值对序列,这边得把之前的dict清除
print(dict3)







