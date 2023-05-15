from time import sleep

""""""

arq_cadastro_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADASTRO_CLIENTE.txt'


class SalaCinema:

    def __init__(self):
        self.quebra_loop = True
        self.linhas_aparencia = '--' * 40

        def leiaInt(valor_int):
            while True:
                try:
                    valor_correto = int(input(valor_int))
                    return valor_correto
                except ValueError:
                    print('Valor incorreto. Digite novamente.')

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
            cinema_sala = [cadeiras_cinema_a, cadeiras_cinema_b, cadeiras_cinema_c, cadeiras_cinema_d,
                           cadeiras_cinema_e,
                           cadeiras_cinema_f, cadeiras_cinema_g, cadeiras_cinema_h, cadeiras_cinema_i,
                           cadeiras_cinema_j]
            return cinema_sala

        def gravando_arq():
            try:
                gravando_dados = open(arq_cadastro_local, 'a')
                gravando_dados.write(f'{self.cpf} ; {self.nome} ; {self.idade} ; {self.email} \n')
                resp = input('Deseja realizar outro cadastro [S/N]: ').upper()
                if resp == 'S':
                    return True
            except:
                print('Não foi possível cadastrar seu usuário')
            else:
                print('Cadastro realizado com sucesso!!')

        def lendo_arq():
            self.dicionario_cliente = dict()
            self.lista_cliente = list()
            try:
                leitura = open(arq_cadastro_local, 'r')
            except:
                print('Erro ao abrir o arquivo')
            else:
                for linha in leitura:
                    dados = linha.split(';')
                    cpf_read = int(dados[0])
                    nome_read = str(dados[1])
                    idade_read = int(dados[2])
                    email_read = str(dados[3])
                    self.dicionario_cliente = {'Nome:': nome_read,
                                               'CPF:': cpf_read,
                                               'Idade:': idade_read,
                                               'E-mail:': email_read}
                    self.lista_cliente.append(cpf_read)

        def cadastro_cliente():
            while True:
                self.nome = input('Digite seu nome completo: ').title()
                self.cpf = leiaInt('Digite seu CPF: ')
                self.idade = leiaInt('Digite sua idade: ')
                self.email = input('Digite seu e-mail: ')
                resp = gravando_arq()
                if not resp:
                    break

        def registro_de_reserva():
            print('<desenvolvimento>')

        def reservar_cadeira():

            lendo_arq()
            while True:
                print(self.linhas_aparencia)
                print('Entre com seu CPF para reservar um poltrona')
                cpf_cliente_reserva = leiaInt('Digite seu CPF: ')
                for cpf_sistema_verifica in self.lista_cliente:
                    if cpf_sistema_verifica == cpf_cliente_reserva:
                        self.confirmado_cpf_no_cadastro = cpf_sistema_verifica
                        self.stop_verif_cpf = True
                        break
                    else:
                        self.quebra_loop = False
                if self.quebra_loop:
                    print('Cadastro encontrado')
                    break
                else:
                    break

            while True:
                if not self.quebra_loop:
                    print(f'Não foi encontrado seu cadastro com o CPF {cpf_cliente_reserva}')
                    print('Faça um cadastro e depois volte!')
                    break
                # Estruturando a sala de cinema
                print(self.linhas_aparencia)
                print(f'TELA'.center(80))
                print(self.linhas_aparencia)
                print()
                for linhas in cinema:
                    print()
                    for coluna in linhas:
                        print(f'[{coluna}] ', end='   ')
                print(f'\n{self.linhas_aparencia}')
                entrada = str(input('Escolha uma Poltrona (999 SAIR): ').upper())
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
                        self.inf_reserva = [cinema[valor_linha][valor_coluna]]
                        if entrada == '999':
                            break
                        elif cinema[valor_linha][valor_coluna] == '--':
                            resp = \
                                str(input(
                                    'Poltrona esta reservada para outra pessoa! Deseja reservar outra? [S/N]: ')).upper()[
                                    0]
                            if resp == 'N':
                                print('Não é possível reservar essa poltrona, reserve outra poltrona')
                                sleep(1)
                        else:
                            cinema[valor_linha][valor_coluna] = str('--')
                    except TypeError:
                        print('Dados informado esta incorreto!')
                except TypeError:
                    print('Dados informados esta incorreto!')
                else:
                    print(f'Poltrona {self.inf_reserva} foi reservada para')

        # Iniciando o programa do zero
        cinema = sala_cinema()

        # Menu principal

        while True:
            print(
                '''
                [1] Reservar uma Poltrona
                [2] Cadastrar um usuário
                [3] Sair
                ''')
            try:
                resp_menu_principal = int(input('Escolha uma opção: '))
                if resp_menu_principal == 1:
                    reservar_cadeira()
                elif resp_menu_principal == 2:
                    cadastro_cliente()

            except TypeError:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
