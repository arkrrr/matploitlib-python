import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# membuat plot
plt.plot(sudut,y)
plt.ylabel("magnitudo")
plt.xlabel("sudut")

plt.yticks([-1,0,1])
plt.xticks(
		[0, 90, 180, 270, 360],
		[r"$ {0}ˆo $",r"$ {90}ˆo $",r"$ {180}ˆo $",r"$ {270}ˆo $",r"$ {360}ˆo $"]
		)


# menampilkan plot
plt.show()