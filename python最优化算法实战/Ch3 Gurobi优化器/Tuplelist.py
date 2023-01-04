# -*- coding:utf-8 -*-

import gurobipy as grb

# 创建tuplelist对象
t1 = grb.tuplelist([(1,2),(1,3),(2,3),(2,5)])

print(t1.select(1,'*'))

print(t1.select('*',3))

t1.append((3,5))
print(t1.select(3,'*'))

print(t1.select(1,'*'))