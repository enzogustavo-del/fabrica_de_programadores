arquivo = open("arquivo.txt", "W", encoding="utf-8")
# "w" cria o arquivo, caso ja exista ele substitui
# "a" append, adiciona ao final. importante usar \n
nome = input("Digite seu nome: \n")
nota = int(input("Digite a nota: \n"))
arquivo.write("-"*20)
arquivo.write(f"\nAluno: {nome}\n")
arquivo.write(f"\nNota: {nota}\n")
arquivo.write("-"*20)


