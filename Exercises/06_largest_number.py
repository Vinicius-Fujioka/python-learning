print("Digite dois numeros para descobrir qual o maior")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 < num2:
    print("O maior numero é: ", num2)
elif num1 == num2:
    print("Os numeros sao iguais")
else:
    print("O maior numero é: ", num1)