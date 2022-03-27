'''
Ex 24
faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.
'''
print ('===== EXERCÍCIO 24 =====\n')
nome = input('Digite um nome completo: ').strip()
#tirar os espaços das extremidades
nomediv = nome.split()
#dividir a frase em blocos pelos espaços
print ('Primeiro Nome: {}'.format(nomediv[0]))
#nomediv[0] vai mostrar a palavra que esta na posição 0
print ('Último Nome: {}'.format(nomediv[len(nomediv)-1]))
#len(nome) = o numero de blocos que existem
#nomediv[len(nome)] = mostrar o bloco no valor de len(nome)
#tira '1' pois a contagem do split começa no '0' mas a do len(nome) começa no '1'.
