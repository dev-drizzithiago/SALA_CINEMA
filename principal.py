from time import sleep
from datetime import datetime
data = datetime.now()
data_atual = data.strftime('%d/%m/%y - %H:%M')
print(data_atual)

""""""

arq_cadastro_cliente_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADASTRO_CLIENTE.txt'
arq_cadastro_registro_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/REGISTRO_RESERVAS.txt'


class SalaCinema:

    def __init__(self):
        self.quebra_loop = True
        self.info_reserva = None
        self.linhas_aparencia = '--' * 40
        self.inf_reserva = list()

        def leiaInt(valor_int):  # Verificar se o valor digitado é 'numero inteiro'
            while True:  # loop_01
                try:
                    valor_correto = int(input(valor_int))
                    return valor_correto
                except ValueError:
                    print('Valor incorreto. Digite novamente.')

        def sala_cinema():  # A montagem do programa
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

        def gravando_dados_no_arq_txt():  # Pega Todos os dados digitado e grava no arquivo txt
            try:
                gravando_dados = open(arq_cadastro_cliente_local, 'a')
                gravando_dados.write(f'{self.cpf} ; {self.nome} ; {self.idade} ; {self.email} \n')
                resp = input('Deseja realizar outro cadastro [S/N]: ').upper()
                if resp == 'S':
                    return True
            except:
                print('Não foi possível cadastrar seu usuário')
            else:
                print('Cadastro realizado com sucesso!!')

        def lendo_dados_no_arq_txt():
            self.dicionario_cliente = dict()
            self.lista_cpf_cliente = list()
            self.lista_dados_cliente = list()

            try:
                leitura = open(arq_cadastro_cliente_local, 'r')
            except:
                print('Erro ao abrir o arquivo')
            else:
                # for_001
                for linha in leitura:
                    dados = linha.split(';')
                    cpf_read = int(dados[0])
                    nome_read = str(dados[1])
                    idade_read = int(dados[2])
                    email_read = str(dados[3])
                    self.lista_cpf_cliente.append(cpf_read)
                    self.lista_dados_cliente.append([cpf_read, nome_read, idade_read, email_read])

        def cadastro_cliente():
            while True:  # loop_02
                self.nome = input('Digite seu nome completo: ').title()
                self.cpf = leiaInt('Digite seu CPF: ')
                self.idade = leiaInt('Digite sua idade: ')
                self.email = input('Digite seu e-mail: ')
                resp = gravando_dados_no_arq_txt()
                if not resp:
                    break

        def registro_de_reserva():
            print('<desenvolvimento>')
            print(self.add_registro_reserva)
            registrando_reserva = open(arq_cadastro_registro_local, 'a')
            registrando_reserva.write(f'{self.add_registro_reserva}\n')
            registrando_reserva.close()

        def reservar_cadeira():
            self.add_registro_reserva = list()
            global valor_linha, valor_coluna
            lendo_dados_no_arq_txt()
            dados_cliente_confirmado = dict()
            while True:  # loop_03

                # Inicia a verificação do cadastro.
                self.quebra_loop = True
                print(self.linhas_aparencia)
                print('Entre com seu CPF para reservar um poltrona')
                cpf_cliente_reserva = leiaInt('Digite seu CPF: ')

                #  for_002
                #  Pega todos os cpf registrados e verifica com o informado pelo cliente
                for cpf_sistema_verifica in self.lista_cpf_cliente:
                    if cpf_sistema_verifica == cpf_cliente_reserva:

                        # Apos a confirmação. O CPF é colocado na variável para ser usado mais a frente
                        self.confirmado_cpf_no_cadastro = cpf_sistema_verifica
                        self.quebra_loop = True  # Se tudo esta certo, quebra-se o loop_03
                        break  # Quebra apenas o loop 'for_002' quando encontra o cpf do cliente
                    else:
                        # Caso não encontrar o cpf, ele colocar a variável como falso, quebrando o loop_03
                        self.quebra_loop = False

                if self.quebra_loop:  # Quebra o loop_03
                    print('Seu cadastro encontrado')
                    break
                else:
                    break

            while True:
                # Caso não encontre o CPF informado pelo cliente
                if not self.quebra_loop:  # Recebe a posição do for_002, se for falso. Quebra o loop_03. Final da fila, recebe o break
                    print(f'Não foi encontrado nenhum cadastro com o CPF informado {cpf_cliente_reserva}')
                    sleep(1)
                    print('Faça um cadastro e depois volte!')
                    sleep(1)
                    break  # Volta para o menu principal, onde o cliente deve fazer um cadastro.

                # Estruturando a sala de cinema para que o cliente visualize as poltronas livres e reservadas
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
                    valor_coluna = int(entrada[1])

                    # Verificar se lugar esta disponível. Caso esteja livre, adiciona os dados no registro.
                    if cinema[valor_linha][valor_coluna] != '--':
                        self.inf_reserva.append(cinema[valor_linha][valor_coluna])

                    # Verificar se o lugar está ocupado. Caso esteja, pede para reservar outro.
                    if cinema[valor_linha][valor_coluna] == '--':
                        print('Não é possível reservar essa poltrona, reserve outra poltrona')
                        sleep(1)
                    else:  # Se o lugar estiver livre. Marca o local com o simbolo.
                        cinema[valor_linha][valor_coluna] = str('--')
                except:
                    print('OS Dados que você informou estão incorretos!')

                # Vai jogar na variável os dados dos cliente e ser mostrado conforme a opção
                for dados_cliente in self.lista_dados_cliente:
                    if dados_cliente[0] == self.confirmado_cpf_no_cadastro:
                        dados_cliente_confirmado['Nome:'] = dados_cliente[1]
                        dados_cliente_confirmado['CPF:'] = dados_cliente[0]
                        dados_cliente_confirmado['Idade:'] = dados_cliente[2]
                        dados_cliente_confirmado['E-mail:'] = dados_cliente[3]
                        self.lista_cliente_reservados = [dados_cliente_confirmado]

                if entrada == '999':
                    if len(self.inf_reserva) == 0:
                        print('Nenhuma poltrona foi reservada!')
                        break
                    else:
                        self.add_registro_reserva.append(self.lista_cliente_reservados)
                        self.add_registro_reserva.append(self.inf_reserva)
                        if len(self.inf_reserva) == 1:
                            print(f'Poltrona {self.inf_reserva} foi reservada para', end='')
                            for chave, valor in dados_cliente_confirmado.items():
                                print(f'{chave}{valor}', end=' ')
                            registro_de_reserva()
                            break

                        else:
                            print(f"As seguintes poltrona's {self.inf_reserva} foram reservadas", end=' ')
                            for chave, valor in dados_cliente_confirmado.items():
                                print(f'{chave}{valor}', end=' ')
                            registro_de_reserva()
                            break

        # Iniciando o programa do zero
        cinema = sala_cinema()

        # Menu principal

        while True:
            print(
                '''
                [1] Reservar uma Poltrona
                [2] Cadastrar um usuário
                [3] Veja suas reservas
                [0] Sair
                ''')
            try:
                resp_menu_principal = int(input('Escolha uma opção: '))
                if resp_menu_principal == 1:
                    reservar_cadeira()
                elif resp_menu_principal == 2:
                    cadastro_cliente()
                elif resp_menu_principal == 3:
                    print('<em desenvolvimento>')
                elif resp_menu_principal == 0:
                    print('Fechando o programa')
                    sleep(1)
                    break
            except TypeError:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
