import matplotlib.pyplot as plt

import pandas as pd

gas = pd.read_csv('gas_prices.csv')

plt.plot(gas.Year,gas.USA,'r.-')
plt.title("Gas Prices")
plt.show()