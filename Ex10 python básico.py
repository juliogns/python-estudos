'''
Ex10
crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
'''


print ('===== EXERCÍCIO 10 =====')
r = float(input('Quantos reais você tem? '))
d = r / 5
print ('Com R${} você consegue comprar U${}.\n\nObs.: >>>Cotação do Dólar em "Mar.2022" = R$5.0<<<'.format(r, d))
