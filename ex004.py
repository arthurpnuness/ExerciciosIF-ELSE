'''
Um professor quer fazer um algoritmo para testar se uma questão de múltipla escolha está certa. Para isso, leia a questão assinalada pelo aluno e verifique:
A - resposta errada
B - resposta certa
C - resposta errada
D - resposta errada
'''

print('Qual foi o ano em que o brasil foi Campeao Da Copa do Mundo? ')
print('A para 2006')
print('B para 2002')
print('C para 1998')
print('D para 1994')
opcao = input('Digite a sua resposta: ').upper()

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

