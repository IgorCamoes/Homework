# Gere um número secreto de 1 a 50 onde o usuário terá que adivinhar esse número

from random import randint

nmrSecreto = randint(1, 50)

i = 5

print("Sejam bem-vindos ao jogo do número secreto")

while i > 0:
    nmrPalpite = int(input(f"Você tem {i} tentativas para adivinhar, qual o seu palpite? "))
    if nmrPalpite > nmrSecreto:
        print(f"O número {nmrPalpite} é MAIOR que o número secreto.")
    elif nmrPalpite < nmrSecreto:
        print(f"O número {nmrPalpite} é MENOR que o número secreto.")
    else:
        break
    i-=1

if i == 0:
    print(f"Infelizmente você excedeu o número de tentativas, o número secreto era {nmrSecreto}")
else:
    print(f"Parabéns você acertou!, o número secreto era {nmrSecreto}!")