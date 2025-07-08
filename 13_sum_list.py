lista = []
for a in range(5,0,-1):
    lista.append(int(input("Por favor, digite " + str(a) + " números: ")))

print("A soma dos números da lista é: " + str(sum(lista)))
print("O maior valor da lista é: " + str(max(lista)))
print("O menor valor da lista é: " + str(min(lista)))
