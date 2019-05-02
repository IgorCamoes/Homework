escada = []
degrais = 5

while degrais >= escada.len:
    escada.append('#')
    print(escada)

usuarioDegrais = int(input("Quantos degrais tem nessa escada? "))

if usuarioDegrais == degrais:
    print("Parabéns, você acertou!")
else:
    print("Infelizmente, você errou, a escada tem " + degrais + " degrais.")

usuarioMaterial = input("Qual é o material (caractere) usado para construir essa escada? ")

if usuarioMaterial == escada[0]:
    print("Parabéns, você acertou!")
else:
    print("Que pena, O material usado foi: " + escada[0])