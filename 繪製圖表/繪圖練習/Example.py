import matplotlib.pyplot as plt
import numpy.random as rand
maxCount = 200
x, y, color = rand.random(maxCount),rand.random(maxCount),rand.random(maxCount)
data1 = list(i*i for i in range(10))
data2 = list((i+i+1) for i in range(10))
plt.figure(1)
plt.scatter(x,y,c=color)
plt.figure(2)
plt.plot(x)
plt.title('plot Example')
plt.figure(3)
plt.plot(x,y)
plt.figure(4)
plt.plot(x[:len(data1)],data1,y[:len(data2)],data2)
plt.show()