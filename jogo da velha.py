p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p_reset = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def layout(a):
    print(f'       |       |       ')
    print(f'   {a[0]}   |   {a[1]}   |   {a[2]}   ')
    print(f'_______|_______|_______')
    print(f'       |       |       ')
    print(f'   {a[3]}   |   {a[4]}   |   {a[5]}   ')
    print(f'_______|_______|_______')
    print(f'       |       |       ')
    print(f'   {a[6]}   |   {a[7]}   |   {a[8]}   ')
    print(f'       |       |       ')
    
def win(a):

    if p[0] == a and p[1] == a and p[2] == a:
        return True
    elif p[3] == a and p[4] == a and p[5] == a:
        return True
    elif p[6] == a and p[7] == a and p[8] == a:
        return True
    elif p[0] == a and p[3] == a and p[6] == a:
        return True
    elif p[1] == a and p[4] == a and p[7] == a:
        return True
    elif p[2] == a and p[5] == a and p[8] == a:
        return True
    elif p[0] == a and p[4] == a and p[5] == a:
        return True
    elif p[2] == a and p[4] == a and p[6] == a:
        return True
    return False
    
def jogada(a):

    jogada = True

    while jogada == True:
        try:
            player = int(input(f'\nplayer {a} de 1-9: ')) - 1
            if player >= 0 and player <= 8:
                 if isinstance(p[player], int) == True:
                    p[player] = a
                    break
                 else:
                    print('já foi escolhido')
            else:
                print('digito errado')
        except:
            print('NÚMERO DE 1-9')
            
def pular_linha(quant):
    for x in range(quant):
        print('\n')
            
jogo = True

while jogo == True:
    layout(p)

    jogada('X')
        

    if win('X') == True:
        pular_linha(50)
        layout(p)
        dnv = input('\nJogador X ganhou! \nJogar denovo? (Y/N): ')
        if dnv.upper() == 'Y':
            p = p_reset
        else:
            jogo = False
            break
        
    pular_linha(50)
        
    layout(p)

    jogada('O')

    if win('O') == True:
        pular_linha(50)
        layout(p)
        dnv = input('\nJogador O ganhou! \nJogar denovo? (Y/N): ')
        if dnv.upper() == 'Y':
            p = p_reset
        else:
            break
        
    pular_linha(50)
