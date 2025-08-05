#Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';



nome = input ('Digite seu nome: ')
while len(nome)<3:
    nome = input ('Digite seu nome: ')
    print(f'Digite um nome maior.')
    
idade = int(input ('Digite sua idade: '))

while idade <= 0 or idade >= 150:
    idade = int(input ('Digite sua idade: '))
    print('DIgite um valor pra idade válido')
    
salario = int(input('Digite seu salário: ')) 
while salario <= 0:
    salario = int(input('Digite seu salário: '))
    print('Digite um valor válido')
    
sexo = input('Digite seu sexo: ')
while sexo == ["f", "m", "trans"]:
    sexo = input('Digite seu sexo: ')
    print('Digite seu sexo corretamente porra')



civil = input('Digite seu estado civíl: ')

if civil == ["s"]:
    print('Solteiro(a), hmmm')

elif civil == ["c"]:
    print('Casado(a), hmmm')

elif civil == ["v"]:
    print('viuvo(a), que triste')

elif civil == ["d"]:
    print('divvorciado(a), hmmm')


