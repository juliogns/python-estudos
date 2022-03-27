'''
Ex 19
crie um programa que leia o nome completo de uma pessoa e mostre:
> o nome com todas as letras maiusculas.
> o nome com todas minusculas.
> quantas letras ao todo(sem considerar espaços)
> quantas letras tem o primeiro nome.
'''
print ('===== EXERCÍCIO 19 =====\n')
nome = input('Informe seu nome completo: ').strip()
#.strip para retirar os espaços das extremidades da frase caso exista.
print ('Caixa Alta: {}'.format(nome.upper()))
print ('Caixa Baixa: {}'.format(nome.lower()))
print ('Letras nome completo: {}'.format(len(nome)-nome.count(' ')))
print ('Letras primeiro nome: {}'.format(nome.find(' ')))
#função find vai localizar o primeiro espaço da frase e mostrar quantos caracteres tem antes, logo = a quantidade de letras do primeiro nome.
