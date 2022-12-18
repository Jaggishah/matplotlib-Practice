import matplotlib.pyplot as plt
import numpy as np
x =[ 1,2,3,4]
y = [3,4,5,6]
x2 = np.arange(0,5,0.5)

plt.plot(x,y ,label = "jaggi", linewidth = 5,marker= '.',linestyle = '--')
plt.plot(x2,x2**2, label = "att")
plt.title("My first Graph",fontdict={'fontsize':'7'})
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.savefig("mypic.png",dpi = 300)
plt.show()