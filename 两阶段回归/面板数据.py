# -*- coding:utf-8 -*-

'''
from linearmodels.panel import PanelOLS
from linearmodels.datasets import wage_panel
import statsmodels.api as sm

data = wage_panel.load()
data = data.set_index(['nr','year'])
dependent = data.lwage
exog = sm.add_constant(data[['expersq', 'married', 'union']])
# mod = PanelOLS(dependent, exog, entity_effects=True)
# res = mod.fit(cov_type='unadjusted')
# print(res)

mod = PanelOLS.from_formula('lwage ~ 1 + expersq + union + married + EntityEffects',data)
res = mod.fit(cov_type='unadjusted')
print(mod)
'''

import wooldridge as woo
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

crime2 = woo.dataWoo('crime2')

# 创建个体索引
id_tmp = np.linspace(1, 46, num=46)
crime2['id'] = np.sort(np.concatenate([id_tmp, id_tmp]))

# 对每个个体的crmrte and unem进行一阶差分
crime2['crmrte_diff1'] = \
    crime2.sort_values(['id', 'year']).groupby('id')['crmrte'].diff()
crime2['unem_diff1'] = \
    crime2.sort_values(['id', 'year']).groupby('id')['unem'].diff()

# statsmodels估计一阶差分模型:
reg_sm = smf.ols(formula='crmrte_diff1 ~ unem_diff1', data=crime2)
results_sm = reg_sm.fit()
print(results_sm.summary())
