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

print(sequenciaSenha)
print('Bem vindo ao jogo da senha secreta!')

while tentativas < 6:
    print(f'Você tem {5 - tentativas} tentativas')
    pos = 1
    for posicao in sequenciaSenha:
        sequenciaUsuario.append(int(input(f'Digite o número que vai na posição numero {pos} ')))
        pos+=1
    
    print(sequenciaUsuario)

    for numero in sequenciaUsuario:
        index = 0
        if numero in sequenciaSenha and numero == sequenciaSenha[index]:
            respostaVisual[index] = 'O'
            print('PRIMEIROIF')
        elif numero in sequenciaSenha and numero != sequenciaSenha[index]:
            respostaVisual.append("-")
            print('SEGUNDOIF')
        elif numero not in sequenciaSenha:
            respostaVisual.append("X")
            print('ULTIMO IF')
    

    print("Resultado da rodada: ")
    print(sequenciaUsuario)
    print(respostaVisual[0:6])

    sequenciaUsuario.clear()
    respostaVisual.clear()

    tentativas+=1
    pos = 0
