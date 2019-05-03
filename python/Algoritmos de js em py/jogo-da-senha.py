from random import randint

provaRealSenha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sequenciaSenha = []
sequenciaUsuario = []
respostaVisual = []
tentativas = 10

while len(sequenciaSenha) < 5:
    a = randint(0,10)
    for digito in provaRealSenha:
        if a in provaRealSenha:
            provaRealSenha.remove(a)
            sequenciaSenha.append(a)

print('Bem vindo ao jogo da senha secreta!')

while tentativas > 0:
    print(f'Voce tem {tentativas} tentativas')
    
    while len(sequenciaUsuario) < 5:
        respostaUsuario = input('Digite sua sequencia de 5 digitos: ')


        for tentativa in respostaUsuario:
            sequenciaUsuario.append(int(tentativa))

        if len(sequenciaUsuario) != 5:
            print('Sequencia invalida, ela deve conter 5 digitos.') 
    
    print(sequenciaUsuario)

    for numero in sequenciaUsuario:

        if numero in sequenciaSenha and sequenciaUsuario.index(numero) == sequenciaSenha.index(numero):
            respostaVisual.append('O')
        elif numero in sequenciaSenha and sequenciaUsuario.index(numero) != sequenciaSenha.index(numero):
            respostaVisual.append('-')
        elif numero not in sequenciaSenha:
            respostaVisual.append('X')



    print('Resultado da primeira rodada: ') 
    print(sequenciaUsuario)
    print(respostaVisual)

    tentativas-=1

    if sequenciaSenha == sequenciaUsuario:
        break

    sequenciaUsuario.clear()
    respostaVisual.clear()

if sequenciaSenha == sequenciaUsuario:
    print('PARABENS, TU CONSEGUIU!!!')
elif tentativas == 0:
    print(f'Que pena que nao conseguiu adivinhar, a senha era {sequenciaSenha}')