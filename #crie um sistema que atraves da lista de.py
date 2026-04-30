#crie um sistema que atraves da lista de nomes e lista e senhas verifique se ousuario digitado esta na lista e que a senha corresponada ao index do usuario
lista = ["Enzo", "Ryan", "Mike"]
senha_usuario = ["3n--Z0", "Rzin", "MK"]

usuario_digitado = input("Digite seu usuario...\n")
senha_digitada = input("Digite sua senha...\n")

index_usuario = lista.index
index_senha = senha_usuario.index(senha_digitada)

try:
    index_usuario == index_senha
    print("Loguin correto...\n")
except:
    print("Usuario/senha incorretos, tente novamente...\n")

        