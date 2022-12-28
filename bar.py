import matplotlib.pyplot as plt
# good to know
labels = ['A','B','C']
values = [1,3,3,]
plt.figure(figsize=(5,3),dpi=200)
bar = plt.bar(labels,values)
# bar[0].set_hatch('/')
patterns = ['/','o','*']
for ba in bar:
    ba.set_hatch(patterns.pop())
plt.xlabel("America")
plt.ylabel("Canada")
plt.savefig("bar.png")
plt.show()