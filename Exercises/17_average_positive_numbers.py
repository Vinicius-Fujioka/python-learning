import numpy as np

lista = []
positivos = []

while True:
    num = int(input("Por favor digite um número: "))
    if num == -1:
        break
    lista.append(num)

for i in range(len(lista)):
    if lista[i] >= 0:
        positivos.append(lista[i])

media = np.mean(positivos)
print(f"A média dos números positivos digitados é: {media}")