'''
Ex6
crie um algoritmo que leia um numero e mostre o seu
dobro, triplo e raiz quadrada
'''


print ('===== EXERCÍCIO 6 =====')
n = float(input ('Digite um número real: '))
d = n * 2
t = n * 3
rq = n**(1/2)
print ('\nSobre o número "{}" \nO dobro: \
{} \nO triplo: {} \nA raiz quadrada: {}'.format \
       (n, d, t, rq))
