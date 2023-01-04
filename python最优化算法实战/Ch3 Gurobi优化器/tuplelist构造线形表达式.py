# -*- coding:utf-8 -*-

import gurobipy as grb

# tuplelist类型的变量快速创建约束条件
m = grb.Model()
x = m.addVars(3,4,vtype=grb.GRB.BINARY, name='x')
m.addConstrs((x.sum(i, '*') <= 1 for i in range(3)), name='con')
m.update()
m.write('tupledict_vars.lp')
