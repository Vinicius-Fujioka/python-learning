lista = []
positivo = 0
negativo = 0
zeros = 0

for i in range(10,0,-1):
    lista.append(int(input(f"Por favor digite mais {i} números: ")))

for i in range(10):
    if lista[i] < 0:
        negativo += 1
    elif lista[i] > 0:
        positivo += 1
    else:
        zeros += 1

print(f"A quantidade de números negativos é: {negativo}")
print(f"A quantidade de números positivos é: {positivo}")
print(f"A quantidade de números zeros é: {zeros}")