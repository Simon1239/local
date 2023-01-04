# -*- coding:utf-8 -*-
'''
修改h1和h2
'''

import numpy as np
import random
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
    NUM = 100 # 生成数量
    x = [random.uniform(0, 1) for _ in range(NUM)]
    epsilon = [random.gauss(0, 1) for _ in range(NUM)]
    dict = {}
    col_names = []
    function_list = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
    for k,f in enumerate(function_list):
        print('使用函数：m{}'.format(k+1))
        m_result = [f(_) for _ in x]
        sigma_result = [sigma(_) for _ in x]
        y = [m_result[i] + sigma_result[i] * epsilon[i] for i in range(NUM)]

        data_list = []
        h1 = 0.0
        h2 = 0.0
        l = []

        for i in range(50):
            h1 = (np.log(NUM)/NUM)**(1/3) - 0.01*i
            if h1 > 0 and i <= 30:
                h2 = (np.log(NUM) / NUM) ** (2 / 3)
                result = main(x,y)
                l.append(result)
                col_names.append('h1:{},h2:{}'.format(h1,h2))
        dict['m{}'.format(k+1)] = l
    df = pd.DataFrame(dict,index=col_names[:31])
    # df.index = col_names[:50]
    df2 = pd.DataFrame(df.values.T,columns=df.index)
    # print(df2)
    df2.to_csv('/Users/simon/Code/两阶段回归/result-2-3.csv',index=False)
    df2.plot(legend=None)
    # for i in range(df2.shape[0]):
    #     plt.plot(range(10),df2.iloc[:,i])
    plt.show()

                # dict['h1:{},h2:{}'.format(h1,h2)] = result
        # print(dict)
    # with open('/Users/simon/Code/两阶段回归/result-1-3.txt','w') as f:
    #     f.write(str(dict))