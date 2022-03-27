'''
Ex 21
crie um programa que leia o nome de uma cidade e diga se ela começa
ou não com o nome 'santo'.
'''
print ('===== EXERCÍCIO 21 =====\n')
cid = input('Informe o nome de uma cidade: ')
ciddiv = cid.split()
#divide o nome da cidade pelos espaços
cid1 = ciddiv[0]
#pega a primeira partição dessa divisão de palavras
cid1upper = cid1.capitalize()
#deixa a primeira letra em maiuscula para comparar
print ('Santo' in cid1upper)
