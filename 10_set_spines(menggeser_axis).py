import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# membuat plot
plt.plot(sudut,y)
plt.title("grafik sinusoidal")


plt.text(180,1,"magnituda")
plt.text(360,0,"sudut")

plt.yticks([-1,-0.5,0,1])
plt.xticks([0,90,180,270,360],
	[r'${0}ˆo$',r'${90}ˆo$',r'${180}ˆo$',r'${270}ˆo$',r'${360}ˆo$'])

ax = plt.gca()
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')




# menampilkan plot
plt.show()