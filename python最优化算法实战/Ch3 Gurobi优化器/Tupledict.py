# -*- coding:utf-8 -*-

import gurobipy as grb

modle = grb.Model()

#  定义变量下标
t1 = [(1,1),(1,2),(1,3),
      (2,1),(2,2),(2,3),
      (3,1),(3,2),(3,3)]
vars = modle.addVars(t1, name='d')

# 基于元素下标的操作
print(sum(vars.select(1,'*')))