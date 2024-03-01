import random
import numpy as np
import matplotlib.pyplot as plt

N = 20000
cantidad_lanzamientos = 10
casos = np.array([i for i in range(0, cantidad_lanzamientos+1)])
f_absoluta = np.zeros(len(casos))
f_relativa = np.zeros(len(casos))
lanzamiento = np.zeros(cantidad_lanzamientos)

for i in range(0,N):
    # 1 representa cara, o representa sello
    lanzamiento = [random.randint(0,1) for j in range(cantidad_lanzamientos)]
    suma_de_aciertos = np.sum(lanzamiento)
    f_absoluta[suma_de_aciertos] += 1

#Total de lanzamientos = cantidad_lanzamientos * N
total_de_lanzamientos = N
f_relativa = f_absoluta / total_de_lanzamientos
print("Distribucion de probabilidad: ", f_absoluta)


fig = plt.figure()
# add_axes(rect), rect = [x0, y0, width, height] , initial point (x0, y0)
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(casos, f_relativa)
plt.xlabel("numero de aciertos")
plt.ylabel("distribucion de probabilidad")
plt.show()

fr_acumulada = np.zeros_like(f_relativa)
for i in range(len(fr_acumulada)):
    for j in range(0, i + 1):
        fr_acumulada[i] += f_relativa[j]
print("distribucion de probabilidad acumulada: ", fr_acumulada)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.xlabel("numero de aciertos")
plt.ylabel("distribucion de probabilidad acumulada")
ax.bar(casos, fr_acumulada)
plt.show()