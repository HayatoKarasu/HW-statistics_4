import numpy as np
import scipy.stats
import pandas as pd
from matplotlib import pyplot as plt

def mean_confidence_interval(data, confidence = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

plt.figure(figsize=(10, 10))

plt.text(0.01, 0.9, "Доверительный интервал – это тот, который", fontsize=20)
plt.text(0.01, 0.8, "покрывает неизвестный параметр с заданной", fontsize=20)
plt.text(0.01, 0.7, "вероятностью.", fontsize=20)
plt.text(0.01, 0.5, "Выброс - результат измерения, не подпадающий", fontsize=20)
plt.text(0.01, 0.4, "под общее распределение.", fontsize=20)
plt.text(0.01, 0.2, "Межквартильный диапазон (IQR) - это разница", fontsize=20)
plt.text(0.01, 0.1, "между третьим квартилем и первым квартилем", fontsize=20)
plt.text(0.01, 0.01, "набора данных.", fontsize=20)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()

data = pd.read_csv('final_data.csv')
print(data.head(5))

print(data.columns)

print(data['lastsoldprice'])

print(mean_confidence_interval(data['lastsoldprice']))

print(data['lastsoldprice'].quantile(0.5), data['lastsoldprice'].median())

q1 = data['lastsoldprice'].quantile(0.25)
q3 = data['lastsoldprice'].quantile(0.75)
iqr = q3 - q1

low = q1 - 1.5 * iqr
hight = q3 + 1.5 * iqr

print(q1, q3, iqr, low, hight)

is_other = (data['lastsoldprice'] <= low) | (data['lastsoldprice'] >= hight)
print(data[is_other]['lastsoldprice'])

print(data.shape)
