from random import randint

provaRealSenha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sequenciaSenha = []
sequenciaUsuario = []
respostaVisual = []
tentativas = 0

while len(sequenciaSenha) < 5:
    a = randint(0,10)
    for digito in provaRealSenha:
        if a in provaRealSenha:
            provaRealSenha.remove(a)
            sequenciaSenha.append(a)

print('Bem vindo ao jogo da senha secreta!')

while tentativas < 10:
    print(f'Você tem {5 - tentativas} tentativas')
    
    while len(sequenciaUsuario) < 5:
        respostaUsuario = input('Digite sua sequencia de 5 dígitos: ')

        if respostaUsuario == 'sair' or 'SAIR' or 'Sair':
            break

        for tentativa in respostaUsuario:
            sequenciaUsuario.append(int(tentativa))

        if len(sequenciaUsuario) != 5:
            print('Sequência inválida, ela deve conter 5 dígitos.') 
    
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

    if sequenciaSenha == sequenciaUsuario:
        break

    sequenciaUsuario.clear()
    respostaVisual.clear()

if sequenciaSenha == sequenciaUsuario:
    print('PARABENS, TU CONSEGUIU!!!')
elif respostaUsuario == 'sair' or 'SAIR' or 'Sair':
    print(f'Que pena que desistiu, a resposta era: {sequenciaSenha}')