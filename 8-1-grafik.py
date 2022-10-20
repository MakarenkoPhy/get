import numpy as np
import matplotlib.pyplot as plt


arr=[]
with open('data.txt', 'r', encoding="utf-8") as f:
    for line in f:
        arr.append(float(line.strip()))
y=np.array(arr)
x=np.linspace(0, y.size/102.8, num=y.size)
fig,ax=plt.subplots()
ax.plot(x,y,
linewidth=2
)
plt.title("Процесс заряда и разряда конденсатора в RC-цепи")
plt.xlabel("Время, с")
plt.ylabel("Напряжение, В")
plt.text(255,2.2,"Время зарядки=215c\n\nВремя разрядки=145c",fontsize=8)


ax.minorticks_on()
ax.grid(which='major',
color='lightgrey',
linewidth=1)

ax.grid(which='minor',
color='lightgrey',
linestyle=':')

plt.legend('V(t)')


plt.show()
