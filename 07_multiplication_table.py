num = int(input("Digite um número para saber sua tabuada de 1 a 10: "))

for i in range(10):
    print(str(num) + " * " + str(i+1) + " = " + str(num*(i+1)))