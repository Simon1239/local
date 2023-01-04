# -*- coding:utf-8 -*-

import statsmodels.api as sm
# import numpy as np

# 第一种方法
Y = [1,3,4,5,2,3,4]
X = range(1,8)
X = sm.add_constant(X)
wls_model = sm.WLS(Y,X,weights=list(range(1,8)))
results = wls_model.fit()
print(results.params)
print(results.tvalues)
print()

import wooldridge as woo
import numpy as np
crime2 = woo.dataWoo('crime2')

# 创建个体索引
id_tmp = np.linspace(1, 46, num=46)
crime2['id'] = np.sort(np.concatenate([id_tmp, id_tmp]))

# 对每个个体的crmrte and unem进行一阶差分
crime2['crmrte_diff1'] = \
    crime2.sort_values(['id', 'year']).groupby('id')['crmrte'].diff()
crime2['unem_diff1'] = \
    crime2.sort_values(['id', 'year']).groupby('id')['unem'].diff()
# print(crime2)
reg_sm = sm.WLS(crime2['crmrte'],crime2['unem'],weights=list(range(crime2.shape[0])))
res = reg_sm.fit()
print(res.params)
