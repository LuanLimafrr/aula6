#aça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que 
#o usuário informe um valor válido.

continua = True

while True:
    nota = int(input('digite uma nota entre [0 e 10]: '))
    if nota < 0 or nota >10:
        print('DIGITE UM VALOR VÁLIDO !!  !! !!')

    elif nota == 0:
        print('Você tirou zero, burro!')
    else:
        print('Você digitou um valor válido')
        continua = False

