import matplotlib.pyplot as plt
import numpy as np

#membuat data
#camel case
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t1,y1 = sinusGenerator(3,3,4,0)
t2,y2 = sinusGenerator(2,2,4,90)

# membuat plot

# tipe pertama
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend()

# tipe kedua
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")
#plt.legend(loc = "upper right")

# tipe ketiga
#plt.plot(t1,y1, label="sin(0)")
#plt.plot(t2,y2, label="sin(90)")

# tipe keempat
plt.figure(1)
ax = plt.subplot(111)
plt.plot(t1,y1, label="sin(0)")
plt.plot(t2,y2, label="sin(90)")
box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width=0.7, box.height])
plt.legend(loc = "upper center", bbox_to_anchor=(0.5,-0.05))


# menampilkan plot
plt.show()
