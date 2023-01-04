# -*- coding:utf-8 -*-

'''
1、生成二维随机数
2、构建g(.)函数
3、构建异方差
4、非参数估计
5、WLS加权最小二成估计

'''

import numpy as np

np.random.seed(1234)

x1 = np.random.rand(1,10)
x2 = np.random.rand(1,10)

epsilon = np.random.randn(1,10)

def g(x):
    return x - 0.5 * x ** 2

result = g(x2)

y = 2+3*x1+g(x2)+epsilon

# 非参数估计

# WLS估计
