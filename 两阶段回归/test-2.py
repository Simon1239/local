# -*- coding:utf-8 -*-
'''
修改h1和h2
'''

import numpy as np
import random

import pandas as pd

np.random.seed(1234)

def m(x):
    return x - 0.5*(x**2)

def sigma(x):
    return 2*x

def gauss_kernel(x,y,h):
    # 定义高斯核
    return np.exp(-(x - y) ** 2 / (2 * h ** 2))

def main(X,Y):
    step1_result = []
    step2_result = []
    sigma_result2 = [_**2 for _ in sigma_result]
    tmp_sum1 = 0.0
    tmp_sum2 = 0.0
    print('\n')
    print('h1:{},h2:{}'.format(h1,h2))
    # print('sigma估计值', 'sigma真实值')
    # sigma_contant = [1 for _ in range(NUM)]
    for i in range(NUM):
        for j in range(NUM):
            xi = X[j]
            yi = Y[j]
            # x = np.mean(X)
            # x = random.uniform(0,10)
            x = X[i]
            tmp_sum1 += gauss_kernel(xi,x,h1)*yi
            tmp_sum2 += gauss_kernel(xi,x,h1)
        divisor1 = tmp_sum1/tmp_sum2
        step1_result.append(divisor1)

    tmp_sum1 = 0.0
    tmp_sum2 = 0.0

    for i in range(NUM):
        for j in range(NUM):
            xi = X[j]
            yi = Y[j]
            # x = np.mean(X)
            x = X[i]
            # x = random.uniform(0, 10)
            tmp_m = step1_result[i]
            tmp_sum1 += gauss_kernel(xi,x,h2)*((yi-tmp_m)**2)
            tmp_sum2 += gauss_kernel(xi,x,h2)
        divisor2 = tmp_sum1/tmp_sum2
        step2_result.append(divisor2)

    max_result = max([abs(step2_result[i]-sigma_result2[i]**2) for i in range(NUM)])
    return max_result



if __name__ == '__main__':
    # 生成随机数
    NUM = 500 # 生成数量
    x = [random.uniform(0, 10) for _ in range(NUM)]
    epsilon = [random.gauss(0, 1) for _ in range(NUM)]
    m_result = [m(_) for _ in x]
    sigma_result = [sigma(_) for _ in x]
    y = [m_result[i] + sigma_result[i] * epsilon[i] for i in range(NUM)]
    dict = {}
    data_list = []
    h1 = 0.0
    h2 = 0.0
    for i in range(50):
        h1 = (np.log(NUM)/NUM)**(1/3) - 0.01*i
        if h1 > 0:
            h2 = (np.log(NUM) / NUM) ** (1 / 3)
            result = main(x,y)
            dict['h1:{},h2:{}'.format(h1,h2)] = result
    print(dict)
    with open('/Users/simon/Code/两阶段回归/result-1-3.txt','w') as f:
        f.write(str(dict))