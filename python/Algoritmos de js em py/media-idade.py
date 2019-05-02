# Pergunte quantas pessoas existem na turma e quais as idades delas, faça o calculo da média com base nesses dados e informe se a turma é jovem, meio jovem, velha ou anciã

def soma(a, b):
    return a + b

nmrPessoas = int(input("Quantas pessoas existem na sua sala? "))

pessoas = []

while len(pessoas) < nmrPessoas:
    pessoas.append(int(input("Qual a idade mental dessa pessoa? ")))

while len(pessoas) > 1:
    pessoas[0] = soma(pessoas[0], pessoas[1])
    pessoas.remove(pessoas[1])

media = int(pessoas[0]) / nmrPessoas

if media < 25:
    print("Tua turma é xovem")
elif media < 30:
    print("Tua turma é meio xovem")
elif media < 35:
    print("Tua turma é meio velha")
else:
    print("Tua turma é anciã!!!!")