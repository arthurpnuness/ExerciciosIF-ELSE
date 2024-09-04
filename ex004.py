'''Neste código le dois valores. Apresenta algumas opções no menu, onde o usuário seleciona a que quer:  
Somar os dois valores.
Subtrair os dois valores.
Multiplicar os dois valores.
Dividir os dois valores
'''

## Interação com o usuário
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('Escolha qual operação aritmética voce quer fazer')
print('Soma')
print('Subtrair')
print('Multiplicação')
print('Divisão')
opcao = input('Digite a operação que voce queira fazer: ') .upper()

## Estruturas Condicionais e exibição do resultado
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
