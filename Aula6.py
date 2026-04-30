lista = []

print("---Lista de nome(s)---\n\n")


nomes = input("Deseja adicionar nomes a lista?\n\n(sim/não)").lower()

if nomes == "sim":
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    x = input("Digite um nome: \n")
    lista.append(x)
    print(f"A lista de nomes é: {lista}")
else:
    print(f"A lista de nomes é: {lista}")
    print("Até logo...")