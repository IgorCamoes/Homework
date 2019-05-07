escada = []
degrais = 5

while degrais > len(escada):
    escada.append('#')
    print(escada)

print(len(escada))
usuarioDegrais = int(input("Quantos degrais tem nessa escada? "))

if usuarioDegrais == degrais:
    print("Parabéns, você acertou!")
else:
    print(f"Infelizmente, você errou, a escada tem {degrais} degrais.")

usuarioMaterial = input("Qual é o material (caractere) usado para construir essa escada? ")

if usuarioMaterial == escada[0]:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, O material usado foi: {escada[0]}")