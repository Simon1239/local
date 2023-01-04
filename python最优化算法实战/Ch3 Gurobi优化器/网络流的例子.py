# -*- coding:utf-8 -*-

import gurobipy as grb

# 两种商品
commodities = ['Pencils', 'Pens']
# 2个产地+3个目的地
nodes = ['Detroit', 'Denver', 'Boston', 'New York', 'Seattle']

# 网络中每条弧线的容量，使用multidict一次性创建多个字典
arcs, capacity = grb.multidict({
    ('Detroit', 'Boston'):100,
    ('Detroit', 'New York'):80,
    ('Detroit', 'Seattle'):120,
    ('Denver', 'Boston'):120,
    ('Denver', 'New York'):120,
    ('Denver', 'Seattle'):120
})

# 商品在不同弧上的运输成品，是tuplelist形式，可以用select、sum等加快变量选取
cost = {
    ('Pencils', 'Detroit', 'Boston'):10,
    ('Pencils', 'Detroit', 'New York'):20,
    ('Pencils', 'Detroit', 'Seattle'):60,
    ('Pencils', 'Denver', 'Boston'):40,
    ('Pencils', 'Denver', 'New York'):40,
    ('Pencils', 'Denver', 'Seattle'):30,
    ('Pens', 'Detroit', 'Boston'):20,
    ('Pens', 'Detroit', 'New York'):20,
    ('Pens', 'Detroit', 'Seattle'):80,
    ('Pens', 'Denver', 'Boston'):60,
    ('Pens', 'Denver', 'New York'):70,
    ('Pens', 'Denver', 'Seattle'):30,
}

# 商品在不同节点的流入量、流出量、即需求量
# 正数表示产品，负数表示需求量
# 是tupledict形式，可以用select、sum等加快变量选取
inflow = {
    ('Pencils', 'Detroit'):50,
    ('Pencils', 'Denver'):60,
    ('Pencils', 'Boston'):-50,
    ('Pencils', 'New York'):-50,
    ('Pencils', 'Seattle'):-10,
    ('Pens', 'Detroit'):60,
    ('Pens', 'Denver'):40,
    ('Pens', 'Boston'):-40,
    ('Pens', 'New York'):-30,
    ('Pens', 'Seattle'):-30
}

# 创建模型
m = grb.Model('netflow')

# 创建变量
flow = m.addVars(commodities, arcs, obj=cost, name='flow')

# 添加容量约束，可使用迭代表达式
m.addConstrs((flow.sum('*', i, j) <= capacity[i, j] for i, j in arcs), 'cap')

# 调价节点流入=流出的约束
m.addConstrs((flow.sum(h, '*', j) + inflow[h, j] == flow.sum(h, j, '*') for h in commodities for j in nodes), 'nodes')

# 求解模型
m.optimize()

# 输出结果
if m.status == grb.GRB.Status.OPTIMAL:
    solution = m.getAttr('x', flow)
    for h in commodities:
        print('\nOptimal flow for %s:'%h)
        for i, j in arcs:
            if solution[h, i, j] > 0:
                print('%s -> %s: %g'%(i, j, solution[h, i, j]))