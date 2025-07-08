notas = []

for i in range(3):
    notas.append(int(input("Digite uma nota: ")))
    soma = sum(notas)

media = soma/len(notas)
if media >= 7:
    print("Aluno aprovado!")
elif media >=5 and media < 7:
    print("Aluno de recuperação!")
elif media < 5:
    print("Aluno reprovado!")