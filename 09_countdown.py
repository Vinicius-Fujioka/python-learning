num = int(input("Digite um numero para a contagem: "))
print("Contagem regressiva")
for i in range(num, 0 , -1):
    if i == 1:
        print(str(i) + " segundo")
    else:
        print(str(i) + " segundos")