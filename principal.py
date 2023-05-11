from time import sleep

""""""

def cadastro_cliente():
    lista_cliente = list()
    nome = input('Digite seu nome completo: ').title()
    idade = int(input('Digite sua idade: '))
    email = input('Digite seu e-mail: ')
    lista_cliente.append([nome, idade, email])

# A montagem do programa
def sala_cinema():
    cadeiras_cinema_a = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
    cadeiras_cinema_b = ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
    cadeiras_cinema_c = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9']
    cadeiras_cinema_d = ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9']
    cadeiras_cinema_e = ['E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9']
    cadeiras_cinema_f = ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']
    cadeiras_cinema_g = ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9']
    cadeiras_cinema_h = ['H0', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9']
    cadeiras_cinema_i = ['I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
    cadeiras_cinema_j = ['J0', 'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9']
    cinema = [cadeiras_cinema_a, cadeiras_cinema_b, cadeiras_cinema_c, cadeiras_cinema_d, cadeiras_cinema_e,
              cadeiras_cinema_f, cadeiras_cinema_g, cadeiras_cinema_h, cadeiras_cinema_i, cadeiras_cinema_j]
    return cinema


# Iniciando o programa do zero
cinema = sala_cinema()

while True:
    linhas_aparencia = '--' * 40
    print(linhas_aparencia)
    print(f'TELA'.center(80))
    print(linhas_aparencia)
    print()
    for linhas in cinema:
        print()
        for coluna in linhas:
            print(f'[{coluna}] ', end='   ')

    print(f'\n{linhas_aparencia}')
    entrada = str(input('Escolha uma Poltrona (999 SAIR / 888 Menu): ').upper())
    try:
        valor_linha = entrada[0]
        if valor_linha == 'A':
            valor_linha = 0
        elif valor_linha == 'B':
            valor_linha = 1
        elif valor_linha == 'C':
            valor_linha = 2
        elif valor_linha == 'D':
            valor_linha = 3
        elif valor_linha == 'E':
            valor_linha = 4
        elif valor_linha == 'F':
            valor_linha = 5
        elif valor_linha == 'G':
            valor_linha = 6
        elif valor_linha == 'H':
            valor_linha = 7
        elif valor_linha == 'I':
            valor_linha = 8
        elif valor_linha == 'J':
            valor_linha = 9
        try:
            valor_coluna = int(entrada[1])
            if entrada == '999':
                break
            elif cinema[valor_linha][valor_coluna] == '--':
                resp = str(input('Poltrona esta reservada para outra pessoa! Deseja reservar outra? [S/N]: ')).upper()[
                    0]
                if resp == 'N':
                    print('Não é possível reservar essa poltrona, reserve outra poltrona')
                    sleep(1)
            else:
                cinema[valor_linha][valor_coluna] = str('--')
        except TypeError:
            print('Dado informado esta incorreto!')
    except TypeError:
        print('Dados informados esta incorreto!')
