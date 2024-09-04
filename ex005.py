'''Faça um algoritmo que leia dois valores. Posteriormente leia uma opção do menu:  
Somar os dois valores.
Subtrair os dois valores.
Multiplicar os dois valores.
Dividir os dois valores
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

opcao = input('Se voce querer somar os valores digite (soma) - Se voce quer subtrair digite (subtratir) - Se voce quer multiplicar digite (multiplicação) - Se voce quiser dividir digite (divisão): ') .upper()

if opcao == 'SOMA':
    soma = num1 + num2
    print(f'A soma entre {num1} e {num2} é: {soma}')
elif opcao == 'SUBTRAIR':
    sub = num1 - num2
    print(f'A subtração entre {num1} e {num2} é: {sub}')
elif opcao == 'MULTIPLICAÇÃO':
    multi = num1 * num2
    print(f'A soma entre {num1} e {num2} é: {multi}')
else:
    div = num1 / num2
    print(f'A divisão entre {num1} e {num2} é: {div}')
