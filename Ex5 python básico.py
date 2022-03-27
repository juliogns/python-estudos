'''
Ex5
faça um programa que leia um numero inteiro e mostre
na tela o seu sucessor e seu antecessor
'''


print ('===== EXERCÍCIO 5 =====')
n = int(input ('Digite um número inteiro: '))
a = n - 1
s = n + 1
print ('\nO número "{}" tem como \nAntecessor: \
{} \ne Sucessor: {}'.format (n, a, s))
