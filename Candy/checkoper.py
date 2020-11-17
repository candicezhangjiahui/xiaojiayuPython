# 算术运算符
a=21
b=10
c=0
c=a+b
print("1.c的值：", c)
c=a-b
d=a*b
e=a/b
f=a%b
print(c,d,e,f)
g=a**b
print(g)
h=a//b #取整除向下取接近商的整数，9//2=4，-9//2=-5
print(h)

## 比较运算符
x=21
y=10
z=0
if (x==y):
    print("x=y")
else:
    print("x不等于y")
if(x != y):
    print("x不等于y")
else:
    print("x=y")

# 赋值运算符

a1=21
b1=10
c1=0
c1=a1+b1
print(c1)
c1 += a
print(c1)
c1 *= a
print(c1)

# 位运算符：按位运算符是把数字看作二进制来进行计算的，
a2 = 60 # 60=0011 1100
b2 = 13 # 13=0000 1101
print(a2&b2) #12=00001100
print(b2|a2) #61=00111101
print(a2^b2) #49=00110001
print(~a2) # -61=11000011  按位取反，符号部分码也得反https://blog.csdn.net/u011452172/article/details/80822402
print(a2<<2)
print(a2>>2)

# 成员运算符 in / not in
a3 = 10
b3 = 20
list1 = [1, 2, 3, 4, 5]
if (a3 in list1):
    print("变量a3在指定的list1里面")
else:
    print("变量a不再列表中")
if (b3 not in list1):
    print("变量b3不在指定的list中")
else:
    print("变量b3在指定的list中")
a3=2
if(a3 in list1):
    print("a3在list1中")
else:
    print("a3不在指定的list中")

# 身份运算符
a4=[1,2,3]
b4=a4
print(b4 is a4)
print(b4==a4)
b4=a4[:]
print(b4)
print(b4 is a4) # is 用于判断两个变量引用对象是否为同一个

# 运算符的优先级
a=20
b=10
c=15
d=5
e=0
e = (a+b)*c/d
print("(a+b)*c/d运算结果：", e)
e=a+b*c/d
print("a+b*c/d 的值是：", e)

# and 拥有最高的优先级
x=True
y=False
z=False
if x and y or z:
    print("yes")
else:
    print("no")

print(k=0)




