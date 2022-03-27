'''
Ex4
faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele 
'''


print ('===== EXERCÍCIO 4 =====')
any = input ('Digite qualquer coisa: ')
print ('Todas informações sobre "{}"'.format (any))
print ('É alfanumérico?', any.isalnum())
print ('É alfabético?', any.isalpha())
print ('É numérico?', any.isnumeric())
print ('É caixa alta?', any.isupper())
print ('É digital?', any.isdigit())
print ('É decimal?', any.isdecimal())
print ('É indentificador?', any.isidentifier())
print ('É caixa baixa?', any.islower())
print ('É imprimível?', any.isprintable())
print ('Tem espaço?', any.isspace())
print ('É título?', any.istitle())
