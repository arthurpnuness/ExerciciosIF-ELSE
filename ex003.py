'''Faça um algoritmo que leia dois valores e apresente:
O maior deles
O menor deles

Obs. o algoritmo deve verificar se os valores digitados são iguais
'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

if num1 == num2:
    print('Os numeros são iguais')
elif num1 > num2:
    print(f'O maior numero entre eles é o {num1}')
elif num2 > num1:
    print(f'O maior numero entre eles é o {num2}')

