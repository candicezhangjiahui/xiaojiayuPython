# temp = input("不妨猜一下小甲鱼现在心里想的数字：")
# guess = int(temp)
# if guess == 8:
#     print("猜对了")
# else:
#     print("猜错了，我想的是8")
# print("游戏结束")

# 第一次改进方面
# 猜错的时候应该给提示，例如大了或者小了
# 只能猜错一次，应该给多次
# 每次答案最好是随机的

# temp = input("不妨猜一下小甲鱼现在心里想的数字：")
# guess = int(temp)
# if guess==8:
#     print("猜中了")
# else:
#     if guess>8:
#         print("大了")
#     else:
#         print("小了")
# print("game over")

# while循环，可以实现循环,在有限次数中实现
# temp = input("不妨猜一下小甲鱼现在心里想的数字：")
# # guess = int(temp)
# # n=0
# # while guess !=8 & n<=3 :
# #     temp=input("猜错了，重新输入吧")
# #     guess = int(temp)
# #     n=n+1
# #     if guess == 8:
# #         print("猜中了")
# #     else:
# #         if guess > 8:
# #             print("大了")
# #         else:
# #             print("小了")
# # print("game over")

# 每次生成一个随机数 ---引入random模块，里面一个randint
import random
secret=random.randint(1,10)
times = 3
guess= 0
temp = input("不妨猜一下小甲鱼现在心里想的数字：")
guess = int(temp)
while (guess !=secret)& (times>0) :
    temp=input("猜错了，重新输入吧")
    guess = int(temp)
    times=times-1
    if guess == secret:
        print("猜中了")
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
        if times>0:
            print("再试一次吧")
        else:
            print("机会没了")
print("game over")
