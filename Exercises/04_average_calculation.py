from statistics import mean

grades = []
for i in range(1,4):
    grades.append(float(input("Digite a "+ str(i) + "° nota: ")))
    
print("A media do aluno é: ", mean(grades))