import numpy as np
import matplotlib.pyplot as plt

"""
	1.membuat data
	2.membuat plot
	3.menampilkan plot/data
"""

#membuat data
#camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y
	
# membuat plot
t,y = sinusGenerator(1,1,4,0)
plt.plot(t,y)

t1,y1 = sinusGenerator(1,1,4,30)
plt.plot(t1,y1, 'r')

t2,y2 = sinusGenerator(1,1,4,60)
plt.plot(t2,y2, 'b--')

t3,y3 = sinusGenerator(1,1,4,90)
plt.plot(t3,y3, 'g-o')

# menampilkan plot
plt.show()