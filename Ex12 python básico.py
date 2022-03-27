'''
Ex12
faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''


print ('===== EXERCÍCIO 12 =====')
p = float(input('Digite o preço atual: '))
d = p - (p*0.05)
print ('R${} com 5% de desconto fica: R${}'.format(p, d))
