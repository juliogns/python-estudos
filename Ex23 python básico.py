'''
Ex 23
faça um programa que leia uma frase pelo
teclado e mostre:
> quantas vezes aparece a letra 'a'
> em que posiçao ela aparece a primeira vez
> em que posiçao ela aparece a ultima vez
'''
print ('===== EXERCÍCIO 23 =====\n')
frase = input('Digite uma frase: ').strip()
#tirar os espaços das extremidades
frasecompare = frase.replace('A', 'a')
#trocar 'A' por 'a' para comparar apenas os 'a'
print ('Quantos A: {}'.format(frasecompare.count('a')))
print ('Primeira posição: {}'.format(frasecompare.find('a')+1))
#+1 entra pq o sitema conta a primeira letra como '0'
print ('Última posição: {}'.format(frasecompare.rfind ('a')+1))
#comando rfind faz achar o 'a' mais pra direita (r de right)
