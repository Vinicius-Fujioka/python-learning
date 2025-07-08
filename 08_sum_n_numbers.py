N = int(input("Digite um número N: "))
print("Agora digite os números para saber sua soma")
nums = []
result = 0
for i in range(N):
    nums.append(int(input("Digite o " + str(i+1) + "° numero: ")))
    result += nums[i]

print("O resultado é: ", result)
