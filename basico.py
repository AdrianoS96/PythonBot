# -*- coding: cp1252 -*-   para aceitar a acentuação no terminal
print('Olá mundo!')
print(5+3)
variavel1 = 5
variavel2 = 3
soma = variavel1 + variavel2 + 1
quadrado = soma ** 2
print(soma)
print(quadrado)
print(f'A soma é: {soma} e o quadrado é: {quadrado}')

if soma == 8:
    print("A soma é 8")
else:
    print(f'A soma é {soma}')

    for n in range(5):
        print(n)