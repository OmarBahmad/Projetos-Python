print('\033[33m-='*30)
print('PROGRAMA DE CONVERSÃO BINÁRIO, OCTAL E HEXADECIMAL')
print('\033[33m-='*30)
print('\033[37mINSTRUÇÕES: Digite um valor no campo abaixo e então escolha a opção desejada!')
print(""" """)

x = int(input('\033[38mESCREVA UM VALOR INTEIRO: '))
print("""
ESCOLHA UMA OPÇÃO:

1 - BINÁRIO
2 - OCTAGONAL
3 - HEXADECIMAL""")
print('')
y = int(input('A OPÇÃO DESEJADA É: '))

if y == 1:
    print('O NUMERO {} CONVERTIDO PARA  BINÁRIO, É {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('O NÚMERO {} CONVERTIDO PARA OCTAL É {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('O NÚMERO {} CONVERTIDO PARA HEXADECIMAL É {}'.format(x, hex(x)[2:]))
else:
    print('\033[31m VocÊ não escolheu uma opção válida, tente novamente!\033[38m')
