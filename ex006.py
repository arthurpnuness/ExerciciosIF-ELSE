'''
Faça um algoritmo que apresente qual veículo o usuário pode dirigir. Com isso, solicite o tipo da carteira de motorista e apresente:
'''

nome = input('Digite seu nome: ')
print('A - ')
print('B - ')
print('C - ')
print('D - ')
print('E - ')

opcao = input('Digite sua resposta: ').upper()

if opcao == 'A':
    print(f'{nome} voce pode dirigir Motos e Triciclos')
elif opcao == 'B':
    print(f'{nome} voce pode dirigir Carros de Passeio')
elif opcao == 'C':
    print(f'{nome} voce pode dirigir Veiculos de Carga acima de 3,5 TON')
elif opcao == 'D':
    print(f'{nome} voce pode dirigir Veiculos com mais de 8 passageiros')
else:
    print(f'{nome} voce pode dirigir Veiculos unidade acoplada acima de 6 TON')







