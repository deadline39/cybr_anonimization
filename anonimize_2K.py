import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
from scipy.stats import norm, expon

data = pd.read_csv('cs200.txt', sep='\t')
data.columns = [x.strip() for x in data.columns]
register_matplotlib_converters()

data['Flow Bytes/s'] = pd.to_numeric(data['Flow Bytes/s'], errors='coerce')
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

array_to_plot = np.array(data['Flow Bytes/s'])
array_to_plot = array_to_plot[~np.isnan(array_to_plot)]
time_group = data.groupby('Timestamp')
print(time_group.describe().index)

plt.xlabel('Timestamp')
plt.ylabel('Flow Bytes/s (sum)')
plt.plot(time_group['Flow Bytes/s'].sum(), linestyle='--', color='grey')
plt.scatter(time_group.describe().index, time_group['Flow Bytes/s'].sum())
plt.show()

plt.xlabel('Timestamp')
plt.ylabel('Flow Bytes/s (mean)')
plt.plot(time_group['Flow Bytes/s'].mean(), linestyle='--', color='grey')
plt.scatter(time_group.describe().index, time_group['Flow Bytes/s'].mean())
plt.show()

mu, sigma = norm.fit(array_to_plot)
ep = expon.fit(array_to_plot)

plt.xlabel('Sample #')
plt.ylabel('Flow bytes/s')
plt.plot(np.arange(len(array_to_plot)), array_to_plot)
plt.show()

x = np.sort(array_to_plot)
y = np.arange(len(x)) / len(x)
plt.xlabel('Flow bytes/s')
plt.ylabel('Empirical CDF')
plt.plot(x, y)
plt.show()

n, bins, _ = plt.hist(array_to_plot, bins=20, density=True)
xr = np.linspace(bins[0], bins[-1], 1000)

plt.plot(xr, norm.pdf(xr, mu, sigma), 'r', label='Gaussian')
plt.plot(xr, expon.pdf(xr, *ep), 'g', label='Exponential')
plt.xlabel('Flow bytes/s')
plt.ylabel('Density')
plt.legend()
plt.plot()
plt.show()