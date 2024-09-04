'''
Neste código foi feito um algoritmo para testar se uma questão de múltipla escolha está certa. Para isso, vamos ler a questão assinalada pelo aluno e verificar:
A - resposta errada
B - resposta certa
C - resposta errada
D - resposta errada
'''

## Interação com o usuário
print('Qual foi o ultimo ano em que o Brasil foi Campeao Da Copa do Mundo? ')
print('A para 2006')
print('B para 2002')
print('C para 1998')
print('D para 1994')
opcao = input('Digite a sua resposta: ').upper()

## Estruturas Condicionais e exibição do resultado
if opcao == 'A':
    print('Resposta incorreta')
elif opcao == 'B':
    print('Resposta Correta, parabéns')
elif opcao == 'C':
    print('Resposta Incorreta')
elif opcao == 'D':
    print('Resposta Incorreta')
else:
    print('Resposta Invalida')

