import matplotlib.pyplot as plt
import random

ab=[]
aa=[]
for i in range(300):
    x = (random.randint(0, 300))
    y = (random.randint(0, 300))
    aa.append(x)
    ab.append(y)
plt.plot(aa,ab,'ro')
plt.axis([0, 300, 0, 300])
plt.show()