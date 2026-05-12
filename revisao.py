# o que são variaveis?

lista = ["Vanessao", "Carlota", "Enzo do pix"]

x = input("Digite seu nome: \n")

if x in lista:
    
    print("O nome digitado esta na lista")

else:
    print("O nome nao esta na lista")

#------------------------------------------------------------#

#2

#VERIFICAR SE O USUARIO PODE VOTAR:


lista = ("Enzo", "Robin", "Amanda")

input("digite sua idade: \n")
if lista:
    if lista <16:
        print("Pode votar")
    else: print("Nao pode votar")
else:
    print("nome de usuario ou idade invalida")

#------------------------------------------------------------#

#3

#lista

minha_futura_garagem = ["BMW", "Mercedes-Bens","Audi", "Aston"]
preco = [35000, 40000, 20000, 80000]

estoque= ["Chevy", "Fiat","Peugeot","Volksvagen","Lexus","Ferrari"]
preço_loja = [1000, 500, 1.99, 20000, 60000, 90000]

loja_barato = []
loja_caro = []

i = 0  #contador

for preco in preço_loja:
    if preco >20000:
        loja_caro.append(estoque[i])
    else:
        loja_barato.append(estoque[i])
    i += 1

    print("loja caro:", loja_caro)
    print("loja barato:", loja_barato)










