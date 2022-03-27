'''
Ex 22
crie um programa que leia o nome de uma pessoa e diga se ela
tem 'silva' no nome.
'''
print ('===== EXERCÍCIO 22 =====\n')
nome = input('Informe um nome completo: ')
nomeupper = nome.title()
#deixa a primeira letra DE CADA PALAVRA em maiuscula para comparar
print ('Silva' in nomeupper)
