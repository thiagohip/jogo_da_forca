from os import system
from random import randint
from time import sleep


def showWLOCK(msg):
    for i in msg:
        print(i, end='')
    print('')


words = ('audaz', 'sanar', 'fosse', 'cerne', 'inato', 'ideia', 'poder',
         'moral', 'desde', 'justo', 'muito', 'sobre', 'torpe', 'honra')


while True:
    print('=-='*15)
    print('\tBEM VINDO AO JOGO DA FORCA')
    print('=-='*15)
    sleep(2)
    wlock = []
    w = words[randint(0, len(words))]
    for j in w:
        wlock.append('_')
    tentativas = 7
    system('cls')
    while True:
        system('cls')
        print(f'Tentativas: {tentativas}')
        showWLOCK(wlock)
        check = 0
        acertou = 0
        flag = 0
        l = input('Digite uma letra: ')
        for i in range(len(w)):
            if l == w[i]:
                wlock[i] = w[i]
                flag = 1

        if flag == 0:
            print('Letra não foi encontrada! Perdeu uma tentiva')
            tentativas -= 1
        else:
            print('A letra foi encontrada')

        for i in range(len(wlock)):
            if wlock[i] == w[i]:
                check += 1
            if check == len(w):
                acertou = 1

        sleep(1)

        if acertou == 1 or tentativas == 0:
            break

    system('cls')
    if acertou == 1:
        showWLOCK(wlock)
        print('Parabens! Você acertou a palavra!')
    else:
        print(f'A palvra era {w}!')
        print('Infelizmente, você não acertou a palavra!')

    op = input('Gostaria de jogar novamente? [S/N] ')
    if op in 'Nn':
        break
