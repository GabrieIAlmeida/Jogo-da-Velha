p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p_reset = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def layout(a):
    print('\n'*100)
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
    elif p[0] == a and p[4] == a and p[8] == a:
        return True
    elif p[2] == a and p[4] == a and p[6] == a:
        return True
    return False
    
def tie():
    for i in p:
        if isinstance(i, int) == True:
            return False
    return True
    
def jogada(a):
    jogada = True
    while jogada == True:
        try:
            player = int(input(f'\nJogador {a} de 1-9: ')) - 1
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
            
def replay():
    p.clear()
    for i in p_reset:
        p.append(i)
    dnv = input('\nJogar Novamente? (y/n): ')
    if dnv.upper() == 'Y':
        jogar()
    else:
        quit()
            
def jogar():
    jogo = True
    
    while jogo == True:
        layout(p)
    
        jogada('X')
        
        if win('X') == True:
            layout(p)
            input('\nJogador X ganhou!')
            replay()
            break
        
        if tie() == True:
            print('\nEmpate!')
            replay()
            
        layout(p)
    
        jogada('O')
    
        if win('O') == True:
            layout(p)
            input('\nJogador O ganhou!')
            replay()
            break
            
        if tie() == True:
            print('\nEmpate!')
            replay()

jogar()
