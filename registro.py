def registroNE():
    file = open("registro.txt","w")
    file = open("registro.txt","r")
    dados = file.readlines()
    file.close()
    file = open("registro.txt","w")
    nome = input("Nome: ")
    email = input("E-mail: ")
    file.write(nome+"\n"+email)
    file.close()
    print("Nome registrado com sucesso")