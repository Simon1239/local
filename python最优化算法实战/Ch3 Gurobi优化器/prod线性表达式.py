# -*- coding:utf-8 -*-

import gurobipy as grb

modle = grb.Model()

#  定义变量下标
t1 = [(1,1),(1,2),(1,3),
      (2,1),(2,2),(2,3),
      (3,1),(3,2),(3,3)]
vars = modle.addVars(t1, name='d')

# 创建一个系数矩阵，用tuplelist格式存储
c1 = [(1,1),(1,2),(1,3)]
coeff = grb.tupledict(c1)
coeff[(1,1)] = 1
coeff[(1,2)] = 0.3
coeff[(1,3)] = 0.4

print(vars.prod(coeff,1,'*'))
