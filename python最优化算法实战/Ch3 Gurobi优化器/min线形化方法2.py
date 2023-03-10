# -*- coding:utf-8 -*-
# 方法2：使用gurobi内置接口方法

import gurobipy as grb

m = grb.Model()
x = m.addVar(name='x')
y = m.addVar(name='y')
z = m.addVar(name='z')
m.addConstr(x == 4, name='c4')
m.addConstr(y == 5, name='c5')
m.addConstr(z == grb.min_(x,y,3))
m.setObjective(z)
m.optimize()
print('最小值是：z=', z.X)