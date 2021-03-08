print('\033[34m-='*30)
print('TABUADA 2.0')
print('-='*30)
print('\033[32mINTRUÇÕES: DIGITE UM VALOR BASE PARA MULTIPLICAÇÃO E EM SEGUIDA O VALOR FINAL DA TABUADA')
x = int(input('\033[mVALOR BASE: '))
n = int(input('\033[mATÉ ONDE A SUA TABUADA VAI?: '))
y = 0
for c in range(0, n+1, 1):
    y += 1
    print('\033[m|{} x {:.2f}| = |{}|'.format(x, y, x*y))
