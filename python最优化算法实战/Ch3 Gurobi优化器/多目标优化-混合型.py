# -*- coding:utf-8 -*-

import gurobipy as grb

model = grb.Model()

x = model.addVar(name='x')
y = model.addVar(name='y')

# 添加第1个目标
model.setObjectiveN(x + 2 * y, index=0, weight=3, priority=20, name='obj1')
# 添加第2个目标
model.setObjectiveN(x - 3 * y, index=1, weight=0.5, priority=1, name='obj2')

for i in range(model.NumObj):
    model.setParam(grb.GRB.Param.ObjNumber, i)
    print('第',i,'个目标的优化值是',model.ObjNVal)