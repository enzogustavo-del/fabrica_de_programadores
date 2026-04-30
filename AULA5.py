print("------Lista da Feira------")

lista = ["Melancia", "Uva"]

opçao = input("Digite uma fruta que voce quer proucurar: \n\n")

if opçao in lista:
    print(f"A fruta {opçao} está na lista...")

else:
    nova_fruta = input(f"A fruta {opçao} não está na lista!!!\n\nVoce quer adicionar uma nova fruta a lista da feira? (sim/não)\n\n").lower

    if nova_fruta == "sim":
        nova_lista = input("Digite a fruta que você quer adicionar: \n\n")
        lista.append(nova_lista)

    else:
        print(f"A lista de frutas da feira é: {lista}")