print('\033[33m-='*30)
print('DESAFIO DOS TRIANGULOS V2.0')
print('-='*30)
print('\033[37mINTRUÇÕES: Adicione 3 lados de um triangulo e descubra se ele existe e qual formato ele tem.')
print('\033[m')
a = int(input('LADO A: '))
b = int(input('LADO B: '))
c = int(input('LADO C: '))
print('')

if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
    if a == b and b == c and a == c:
        print('EQUILATERO')
    elif a == b or b == c or a == c:
        print('ISOSCELES')
    else:
        print('ESCALENO')

#if abs(b-c) >= a >= b+c and abs(a-c) >= b >= a+c and abs(a-b) >= c >= a+b:
#    print('Esse triangulo não pode existir!')
#elif abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and a == b and b == c and a == c:
#    print('\033[1:35mEste triangulo é EQUILATERO!')
#elif abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and (a == b or b == c or a == c):
#    print('\033[1:34mEste triangulo é ISOSCELES!')
#elif abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b and a != b and a != c and b != c:
#    print('\033[1:32mEsse triangulo é ESCALENO!')
else:
    print('\033[31mESSE TRIANGULO NÃO EXISTE!')