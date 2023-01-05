# -*- coding:utf-8 -*-
'''
修改h1和h2
'''

import numpy as np
import random
import json
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(1234)

def m1(x):
    return 0

def m2(x):
    return (3/4)*np.sin(20*np.pi*x)

def m3(x):
    return (3/4)*np.sin(30*np.pi*x)

def m4(x):
    return (3/4)*np.sin(40*np.pi*x)

def m5(x):
    return (3/4)*np.sin(50*np.pi*x)

def m6(x):
    return (3/4)*np.sin(60*np.pi*x)

def m7(x):
    return (3/4)*np.sin(70*np.pi*x)

def m8(x):
    return (3/4)*np.sin(80*np.pi*x)

def m9(x):
    return (3/4)*np.sin(90*np.pi*x)

def m10(x):
    return (3/4)*np.sin(100*np.pi*x)

def sigma(x):
    return (x-1/2)**2+1/2

def gauss_kernel(x,y,h):
    # 定义高斯核
    return np.exp(-(x - y) ** 2 / (2 * h ** 2))

def main(X,Y):
    step1_result = []
    step2_result = []
    sigma_result2 = [_**2 for _ in sigma_result]
    tmp_sum1 = 0.0
    tmp_sum2 = 0.0
    # print('\n')
    # print('h1:{},h2:{}'.format(h1,h2))
    for i in range(NUM):
        for j in range(NUM):
            xi = X[j]
            yi = Y[j]
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
            x = X[i]
            tmp_m = step1_result[i]
            tmp_sum1 += gauss_kernel(xi,x,h2)*((yi-tmp_m)**2)
            tmp_sum2 += gauss_kernel(xi,x,h2)
        divisor2 = tmp_sum1/tmp_sum2
        step2_result.append(divisor2)

    max_result = max([abs(step2_result[i]-sigma_result2[i]**2) for i in range(NUM)])
    return max_result



if __name__ == '__main__':
    # 生成随机数
    N = 100 # 模拟
    NUM = 500  # 生成数量
    function_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
    for k,f in enumerate(function_list):
        dict = {}
        for i in range(50):
            res = []
            h1 = (np.log(NUM) / NUM) ** (1 / 3) - 0.01*i
            h2 = (np.log(NUM) / NUM) ** (1 / 3)
            print('h1:{}, h2:{}'.format(h1, h2))
            if h1 > 0:
                for n in range(N):
                    print('第{}模拟'.format(n))

                    x = [random.uniform(0, 1) for _ in range(NUM)]
                    epsilon = [random.gauss(0, 1) for _ in range(NUM)]

                    m_result = [m2(_) for _ in x]
                    sigma_result = [sigma(_) for _ in x]
                    y = [m_result[i] + sigma_result[i] * epsilon[i] for i in range(NUM)]

                    result = main(x,y)
                    res.append(result)
                median_num = np.median(res)
                dict['h1:{}, h2:{}'.format(h1, h2)] = median_num
        dict_json = json.dumps(dict)
        f = open('/Users/simon/Code/两阶段回归/data/m{}.json'.format(k+1),'w')
        print('保存成功！')
        f.write(dict_json)

