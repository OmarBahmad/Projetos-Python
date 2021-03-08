x = str(input('DIGITE UMA FRASE E DESCUBRA SE É UM PALÍNDROMO:').strip().upper().replace(' ', ''))
print(x)
z = x.count('')
h = list(x)
y = []

for x in reversed(x):
    y.append(x)
print(y)
print(h)
if y == h:
    print('é um palindromo')
else:
    print('não é')

#    print(x)
#    print(c)
#    h = x.split()
#    y.append(h[0][w])
#    w = w + 1
#print(y)
#for c in range(0,):
#z = x.split( 1)
#print(z)
#for c in range(0,):
#print(x)
#n = list(x)
#print(n)
#print(y)
#if y == x:
#    print('A FRASE É UM PALINDROMO!')
#else:
#    print('NÃO É UM PALINDROMO')
