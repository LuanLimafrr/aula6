#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
#de erro e voltando a pedir as informações.,

while True:

    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')

    if senha == nome:
        print('Você digitou a senha igual o nome.')

    else:
        print('Você acertou')

    break
