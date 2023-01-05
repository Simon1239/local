# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import json

legends = []
for i in range(1,10):
    print(i)
    with open('/Users/simon/Code/两阶段回归/data/m{}.json'.format(i), 'r') as f:
        data = f.read()
        jdata = json.loads(data)

    x = []
    y = []
    for k in jdata.keys():
        x.append(eval(k.split(',')[0].split(':')[1]))
        y.append(jdata.get(k))
    plt.plot(x,y)
    legends.append('m{}'.format(i))
plt.xlim(0,0.25)
plt.ylim(0.5,0.9)
plt.legend(legends)
plt.show()
# print(jdata)
