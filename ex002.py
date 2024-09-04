'''Neste código foi feito um algoritmo que le dois valores e apresentamos:
O maior deles
O menor deles
Também o algoritmo deve verificar se os valores digitados são iguais
'''

## Interação com o usuário
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

## Estruturas Condicionais e exibição do resultado
if num1 == num2:
    print('Os numeros são iguais')
elif num1 > num2:
    print(f'O maior numero entre eles é o {num1}')
elif num2 > num1:
    print(f'O maior numero entre eles é o {num2}')

