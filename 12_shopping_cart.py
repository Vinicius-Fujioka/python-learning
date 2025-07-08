
carrinho = []
print("Digite items para adicionar ao carrinho, para sair digite sair: ")
while True:
    item = input()
    if item == "sair":
        break
    carrinho.append(item)

print("Carrinho:")
print("- " + "\n- ".join(carrinho))
