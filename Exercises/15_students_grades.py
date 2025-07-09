alunos = []
soma = 0

for i in range(3):
    nome = input("Por favor digite o nome do aluno: ")
    nota = int(input("Por favor digite a nota do aluno: "))
    alunos.append([nome,nota])

for aluno in alunos:
    soma += aluno[1]    

maior = max(alunos, key=lambda aluno: aluno[1])
menor = min(alunos, key=lambda aluno: aluno[1])

media = soma/len(alunos)

print("A média da turma é: " + str(media))
print(f"O aluno com a maior nota é: {maior[0]}")
print(f"O aluno com a menor nota é: {menor[0]}")
