import matplotlib.pyplot as plt

import pandas as pd
plt.style('ggplot')
fifa = pd.read_csv('fifa_data.csv')
# print(fifa.columns)
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
print(left,right)
labels = ['Left',"Right"]

plt.pie([left,right],labels=labels)
plt.show()