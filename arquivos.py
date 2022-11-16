import os 
def lerNomeEmail():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    historico = open('historico.txt','a')
    historico.write(f'Nome: {nome}\ne-mail: {email}\n\n')
    historico.close()
    os.system('cls')
    return print('Cadastro efetuado com sucesso!')