y = []
mediaidade = []
s = []
for pessoas in range(0, 4):
    nome = str(input('DIGITE O NOME COMPLETO DE UMA PESSOA: ')).strip().upper()
    idade = int(input('DIGITE A IDADE DESSA PESSOA: '))
    sexo = str(input('MASCULINO (M) OU FEMININO (F): ')).strip().upper()
    y.append([nome, idade, sexo])
    mediaidade.append(idade)
    s.append(sexo)
    print('-='*40)
print('A MÉDIA DAS IDADES É DE {}'.format(sum(mediaidade)/4))
#print(y)
#print(len(y))
#print(len(y[0]))
#print(len(y[1]))
#print(len(y[0:1]))
x = 0
mulheres = []
homens = []
#print(mediaidade)
for c in y:
    if 'M' in y[x]:
        homens.append(y[x])

    elif 'F' in y[x]:
        mulheres.append(y[x])
    x = x + 1
#print(homens)
#print(mulheres)
maior = []
for t in homens:
    maior.append(t[1])
#print(maior)
#print(max(maior))
for z in homens:
    if max(maior) == z[1]:
        print('O HOMEM MAIS VELHO É O {}'.format(z[0]))

abx = []
for k in mulheres:
    if k[1] < 20:
        abx.append(k[1])
#print(abx)
print('A QUANTIDADE DE MULHERES ABAIXO DE 20 ANOS É DE {}'.format(len(abx)))
