import matplotlib.pyplot as plt
import numpy as np

#membuat data
#camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t,y = sinusGenerator(2,2,6,0)

# membuat plot
plt.plot(t,y)

# setting axis, minimum sama maximum
# xmin,xmax,ymin,ymax
plt.axis([0,4,-2,2])


# menapilkan plot
plt.show()
