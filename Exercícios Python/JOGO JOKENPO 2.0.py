from time import sleep
import random
print('\033[33m=-'*30)
print('JOKENPO')
print('=-'*30)
print('\033[m')
a = str('PEDRA')
b = str('PAPEL')
d = str('TESOURA')
for c in range(0, 5, 1):
    x = random.choice([a, b, d])
    print('ESCOLHA UMA DAS ALTERNATIVAS PARA JOGAR:')
    print("""    1 - PEDRA
    2 - PAPEL
    3 - TESOURA""")
    print('')
    y = int(input('\033[34mESCREVA UMAS DAS ALTERNATIVAS: ').strip())
    print('PROCESSANDO...')
    print(x)
    sleep(1)
    if (y == 1 and x == 'PEDRA') or (y == 2 and x == 'PAPEL') or (y == 3 and x == 'TESOURA'):
        print('\033[35mVOCÊS EMPATARAM, RESULTADO O COMPUTADOR ESCOLHEU {}'.format(x))
        print('\033[m')
    elif (y == 1 and x == 'TESOURA') or (y == 2 and x == 'PEDRA') or (y == 3 and x == 'PAPEL'):
        print('\033[32mVOCÊ GANHOU, O COMPUTADOR ESCOLHEU {}'.format(x))
        print('\033[m')
    elif (y == 1 and x == 'PAPEL') or (y == 2 and x == 'TESOURA') or (y == 3 and x == 'PEDRA'):
        print('\033[31mVOCÊ PERDEU, O COMPUTADOR JOGOU {}'.format(x))
        print('\033[m')
