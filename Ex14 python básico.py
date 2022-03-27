'''
Ex14
crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira
'''
import math

print ('===== EXERCÍCIO 14 =====')
n = float(input('Digite um número real: '))
i = math.floor(n)
print ('A porção inteira de {} é {}'.format(n, i))
