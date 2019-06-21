# -*- coding:utf-8 -*-
rmb_value_rec = input("输入人民币金额：")
print('rmb_value_rec:',rmb_value_rec)
rmb_value = eval(rmb_value_rec)
ouyuan_vs_rmb = 7.7528
ouyuan_value =rmb_value / ouyuan_vs_rmb
print('欧元：', ouyuan_value)

