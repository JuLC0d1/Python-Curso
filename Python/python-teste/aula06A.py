t1 = int(input('Digite um valor: '))
t2 = int(input('Digite outro valor: '))
s = t1 + t2
# print('A soma de ', t1 , 'e' , t2 , 'vale = ' ,  s) formato antigo, é preferivel a forma abaixo
print('A soma de {} e {} vale {}'.format(t1, t2, s))