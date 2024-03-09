"""
Empezando un juego de parqués, se lanzan dos dados ideales de 6 caras para salir de la
cárcel y se cuentan con tres intentos para obtener dobles (dos números iguales).
a. ¿Cuál es la probabilidad de obtener dobles en el primer lanzamiento?
b. ¿Cuál es la probabilidad de obtener dobles solo hasta el segundo lanzamiento?
c. ¿Cuál es la probabilidad de obtener dobles solo hasta el tercer lanzamiento?
d. Demuestre con un script en Python que se cumple con los resultados teóricos.
Utilice gráficas para mostrar la información.
"""

import random
import numpy as np
import matplotlib.pyplot as plt

N = 200000
casos = np.array([1,2,3])
contador = np.array([0,0,0]) # arreglo con posiciones de 0 a 3
# el for va de 0 a n-1
for i in range(0,N):
    for j in range(0,3):
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        if dado1 == dado2:
            contador[j] += 1
            break


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
print("distribucion de probabilidad relativa: ",fr)
print("distribucion de probabilidad acumulada: ", fr_acumulada)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
plt.xlabel("casos")
plt.ylabel("distribucion de probabilidad acumulada")
ax.bar(casos, fr_acumulada)
plt.show()