"""Un jugador de futbol tiene una probabilidad de acierto del 80% al momento de cobrar un
penalti. ¿Cuál es la probabilidad de que marque por primera vez solo hasta el quinto penalti?"""

import random
import numpy as np
import matplotlib.pyplot as plt

N = 20000
turnos = np.array([0,1,2,3,4,5])
contador = np.array([0,0,0,0,0,0])
fr_relativa = np.zeros_like(contador)

for i in range(0,N):
    for j in range(0,5):
        dado = random.randint(4,5)
        if dado != 5:
            contador[j] += 1
            break

print(contador)
for i in range(len(contador)):
    fr_relativa = contador/float(N)
print(fr_relativa)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(turnos, fr_relativa)
plt.xlabel("Cantidad de lanzamientos antes del acierto")
plt.ylabel("Distribucion de probabilidad")
plt.show()

fr_acumulada = np.zeros_like(fr_relativa)
for i in range(len(fr_acumulada)):
    for j in range(0,i + 1):
        fr_acumulada[i] += fr_relativa[j]

print(fr_acumulada)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(turnos, fr_acumulada)
plt.xlabel("Cantidad de lanzamientos antes del acierto")
plt.ylabel("Distribucion de probabilidad acumulada")
plt.show()