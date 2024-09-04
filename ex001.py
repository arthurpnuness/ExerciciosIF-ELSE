''''Neste código foi feito um sistema de uma loja de roupas permite que as peças de roupas sejam vendidas de três formas diferentes: 
À vista.
2 vezes.
3 vezes.
Para isso, o sistema vai ler o valor da peça, a opção de pagamento e apresentar o valor das parcelas.
'''

## Interação com o usuário
print('Bem vindo a loja do Arthur')
print('1 - Pagar à vista')
print('2 - Pagar em 2x (15 porcento de juros)')
print('3 - Pagar em 3x (30 porcento de juros)')   
opcao = int(input('Digite uma opção: '))

valorCompra = float(input('Digite o valor da compra: '))

## Estruturas Condicionais e exibição do resultado
if opcao == 1:
    valorFinal = valorCompra * 0.5
    print('Valor da compra com desconto R${}'.format(valorFinal))
elif opcao == 2:
    valorFinal = valorCompra * 1.15
    print('Valor da compra com juros R${}'.format(valorFinal))
elif opcao == 3:
    valorFinal = valorCompra * 1.30
    print('Valor da compra com juros R${}'.format(valorFinal))
else:
    print('Opção Inválida!')