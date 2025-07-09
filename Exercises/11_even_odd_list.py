nums = []

for i in range(10,0,-1):
    nums.append(int(input("Digite mais " + str(i) + " numeros:")))

par = []
impar = []

for i in range(10):
    if nums[i] %2 == 0:
        par.append(nums[i])
    else:
        impar.append(nums[i])

print(impar)
print(par)