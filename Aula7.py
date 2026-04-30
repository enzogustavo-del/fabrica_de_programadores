# Aula de index
lista_usuario = ["Vanessa", "Carla", "Enzo"]
senha_do_usuario = ["Van123", "C4rly", "En_z0"]

(lista_usuario).index
(senha_do_usuario).index

digite_seu_usuario = input("Digite seu usuario...\n")
digite_sua_senha = input("Digite sua senha...\n")

(digite_seu_usuario).index
(digite_sua_senha).index

if digite_seu_usuario in lista_usuario and digite_sua_senha in senha_do_usuario:
    print("Logiun concluido...\n")

else:
    print("Senha/usuario incorreta(o), tente novamente...\n")




    