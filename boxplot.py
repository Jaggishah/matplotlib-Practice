import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv('fifa_data.csv')
colors = ['#0000FF', '#00FF00',
          '#FFFF00', '#FF00FF']
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

level1 = data.loc[data.Club == 'FC Barcelona']['Overall']
level2 = data.loc[data.Club == 'Manchester United']['Overall']
print(level1,level2)
boxes1 = plt.boxplot([level1,level2],labels=['jaggi','shah'])
for box in boxes1['boxes']:
    box.set_gapcolor(colors[1])
for cap in boxes1['caps']:
    cap.set(color ='#8B008B',
            linewidth = 2)
for median in boxes1['medians']:
    median.set(color ='red',
               linewidth = 3)

for flier in boxes1['fliers']:
    flier.set(marker ='D',
              color ='#e7298a',
              alpha = 0.5)
     
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.show()