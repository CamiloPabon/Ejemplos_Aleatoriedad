"""En un juego se lanzan tres dados ideales de 6 caras, y se suman los puntos. Gana la persona
que acerte a la suma.
a. ¿A qué número sería adecuado apostar?
b. Demuestre con un script en Python que se cumple con los resultados teóricos.
Utilice gráficas para mostrar la información."""

import random
import numpy as np
import matplotlib.pyplot as plt

N = 200000
casos = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
contador = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# el for va de 0 a n-1
for i in range(0,N):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    suma = dado1 + dado2 + dado3
    contador[suma] += 1

print("suma por caso: ", contador)
fr = contador/N
print("casos de suma", casos)

fig = plt.figure()
# add_axes(rect), rect = [x0, y0, width, height] , initial point (x0, y0)
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.bar(casos, fr)
plt.xlabel("casos")
plt.ylabel("distribucion de probabilidad")
plt.show()

fr_acumulada = np.zeros_like(fr)
for i in range(len(fr_acumulada)):
    for j in range(0, i + 1):
        fr_acumulada[i] += fr[j]
print("distribucion de probabilidad acumulada: ", fr_acumulada)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.xlabel("casos")
plt.ylabel("distribucion de probabilidad acumulada")
ax.bar(casos, fr_acumulada)
plt.show()