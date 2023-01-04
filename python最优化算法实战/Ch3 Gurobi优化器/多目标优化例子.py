# -*- coding:utf-8 -*-

import gurobipy as grb
import numpy as np

# 设定工人数和工作数量
N = 10
np.random.seed(1234)

#用随机数初始化时间矩阵Tij和成本矩阵Cij
Tij = {(i+1, j+1): np.random.randint(0,100) for i in range(N) for j in range(N)}
Cij = {(i+1, j+1): np.random.randint(0,100) for i in range(N) for j in range(N)}

# 定义model
m = grb.Model('MultiObj')

# 添加变量，x是tupledict类型，可以使用select函数，sum函数，prod函数
x = m.addVars(Tij.keys(), vtype=grb.GRB.BINARY, name='x')

# 添加约束
m.addConstrs((x.sum('*', j+1) == 1 for j in range(N)), 'C1')
m.addConstrs((x.sum(i+1,'*') == 1 for i in range(N)), 'C2')

# 多目标方式1：Blend合成型
# m.setObjectiveN(x.prod(Tij), index=0, weight=0.1, name='obj1')
# m.setObjectiveN(-x.prod(Cij), index=1, weight=0.5, name='obj2')

# 多目标方式2：Hierarchical分层型
m.setObjectiveN(x.prob(Tij), index=0, priority=1, abstol=0, reltol=0, name='obj1')
m.setObjectiveN(-x.prob(Tij), index=1, priority=2, abstol=100, reltol=0, name='obj2')

# 启动求解
m.optimize()

# 获取求解结果
for i in Tij.keys():
    if x[i].x > 0.9:
        print('工人 %d 分配工作 %d'%(i[0], i[1]))

# 获取目标函数
for i in range(2):
    m.setParam(grb.GRB.Param.ObjNumber,i)
    print('Obj%d = '%(i+1),m.ObjNVal)
