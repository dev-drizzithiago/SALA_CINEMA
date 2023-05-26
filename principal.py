import threading
from time import sleep
from datetime import datetime

# from threading import Thread

data = datetime.now()
data_atual = data.strftime('%d/%m/%y')
hora_atual = data.strftime('%H:%M:%S')

""""""

arq_cadastro_cliente_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADASTRO_CLIENTE.txt'
arq_cadastro_registro_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/REGISTRO_RESERVAS.txt'


class SalaCinema:

    def __init__(self):
        self.quebra_loop = True
        self.info_reserva = None
        self.linhas_aparencia = '--' * 60
        self.inf_reserva = list()
        self.lista_reserva_cliente = list()

        def aperte_enter():
            input('Aperte ENTER para continuar!')

        def inicio_verif_arq_reserva():
            sleep(0.1)
            if not verificando_arq_registro_reserva():
                print('Estamos criando o arquivo para você')
                sleep(1)
                criando_arq_registro_reserva()
                sleep(1)
                print('Pronto, conseguimos criar o arquivo.\n'
                      'tenha uma boa reserva!!')

        # VERIFICAR SE POSSUI O ARQUIVO RESPONSÁVEL PELO CADASTRO DO CLIENTE.
        def verificar_arq_cadastro_cliente():
            try:
                verificacao = open(arq_cadastro_cliente_local, 'r')
            except:
                return False
            verificacao.close()

        # CASO NÃO EXISTA O ARQUIVO. O PROGRAMA IRA CRIAR UM
        def criando_arq_cadastro_cliente():
            try:
                criando_arq_cliente = open(arq_cadastro_cliente_local, 'w')
            except:
                print('Não foi possível criar um arquivo para guardar seus cadastros')
            else:
                print('Não se preocupe, irei criar um cadastro para você')
                sleep(2)
                print('Prontinho!!')
                sleep(1)
                print('Arquivo para cadastro foi criado!!')
                sleep(1)
                print('Realize seu cadastro e boa reserva!!')
                sleep(1)
                criando_arq_cliente.close()

        def verificando_arq_registro_reserva():
            try:
                verificacao_arq_reserva_txt = open(arq_cadastro_registro_local, 'r')
                verificacao_arq_reserva_txt.close()
                return True
            except:
                return False

        def criando_arq_registro_reserva():
            try:
                criando_arq_registro_reserva_txt = open(arq_cadastro_registro_local, 'w')
            except:
                print('Não foi possível criar o arquivo para registrar suas reservas')
            else:
                criando_arq_registro_reserva_txt.close()

        # Atributos
        def leiaInt(valor_int):  # Verificar se o valor digitado é 'numero inteiro'
            while True:  # loop_01
                try:
                    valor_correto = int(input(valor_int))
                    return valor_correto
                except ValueError:
                    print('Valor incorreto. Digite novamente.')

        # Estrutura para sala de cinema
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

        # Métodos
        def gravando_dados_arq_cliente_txt():  # Pega Todos os dados digitado e grava no arquivo txt
            try:
                gravando_dados = open(arq_cadastro_cliente_local, 'a')
                gravando_dados.write(f'{self.cpf};{self.nome};{self.idade};{self.email}\n')
                print('Cadastro realizado com sucesso!!')
                sleep(0.5)
                resp = input('Deseja realizar outro cadastro [S/N]: ').upper()
                if resp == 'S':
                    return True
            except:
                print('Não foi possível cadastrar seu usuário')
                if not verificando_arq_registro_reserva():
                    criando_arq_registro_reserva()

        def lendo_dados_arq_cliente_txt():
            # Variáveis locais
            self.dicionario_cliente = dict()
            self.lista_cpf_cliente = list()
            self.lista_dados_cliente = list()

            # Função para leitura
            try:
                leitura = open(arq_cadastro_cliente_local, 'r')
            except:
                print('Erro ao abrir o arquivo de cadastro\n'
                      'Arquivo pode estar corrompido ou...\n'
                      'Arquivo não existe')
                sleep(1)
                if not verificar_arq_cadastro_cliente():
                    criando_arq_cadastro_cliente()
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
                leitura.close()

        def lendo_dados_no_arq_reserva():
            self.lista_info_registro = list()
            try:
                leitura = open(arq_cadastro_registro_local, 'r')
            except:
                print(self.linhas_aparencia)
                print('Não foi possível abrir o arquivo que registra as reservas.')
                sleep(0.5)
                print('Deixa eu verificar se o arquivo esta íntegro')
                threading.Thread(target=inicio_verif_arq_reserva()).start()
            else:
                for valor in leitura:
                    self.lista_info_registro.append(valor)
                if len(self.lista_info_registro) == 0:
                    print(self.linhas_aparencia)
                    print('Não encontrei nenhum registro no sistema. '
                          'Verifique se a sessão já terminou')
                    aperte_enter()

        # Manipulações
        def cadastro_cliente():
            while True:  # loop_02
                self.nome = input('Digite seu nome completo:').title()
                self.cpf = leiaInt('Digite seu CPF:')
                self.idade = leiaInt('Digite sua idade:')
                self.email = input('Digite seu e-mail:')
                resp = gravando_dados_arq_cliente_txt()
                if not resp:
                    break

        def registro_da_reserva():
            try:
                registrando_reserva = open(arq_cadastro_registro_local, 'a')
            except:
                print('Não consegui registrar sua reservar.')
                print('Verifiquei o administrador do sistema!')
            else:
                registrando_reserva.write(f'{self.lista_reserva_cliente} ; {data_atual} - {hora_atual}\n')
                registrando_reserva.close()

        # Verificar o arq que contem os registros de reservas
        def consultar_registro_reserva():
            lendo_dados_no_arq_reserva()
            for valor in self.lista_info_registro:
                cpf_consulta = str(valor[1:12]).replace(',', '')
                print(len(cpf_consulta))
                print(cpf_consulta)

        # Corpo do programa
        def reservar_cadeira():
            self.add_registro_reserva = list()
            global valor_linha, valor_coluna, nome_cliente, nome_reservado, cpf_reservado
            lendo_dados_arq_cliente_txt()
            # dados_cliente_confirmado = dict()
            while True:  # loop_03

                # Inicia a verificação do cadastro.
                self.quebra_loop = True
                print(self.linhas_aparencia)
                print('Preciso do seu CPF para reservar uma poltrona.')
                cpf_cliente_reserva = leiaInt('Digite seu CPF: ')

                # CASO NÃO EXISTE NENHUM CADASTRO, PROGRAMA NÃO CONTINUA
                if len(self.lista_cpf_cliente) == 0:
                    print(self.linhas_aparencia)
                    print('- DESCULPE!!! '
                          '- Não encontramos nenhum registro no sistema. \n'
                          '- Verifiquei se o bando de dados esta tudo certinho! \n'
                          '- Caso o bano de dados esteja funcionando normalmente, verifique se você possui cadastro!')
                    aperte_enter()
                    self.quebra_loop = False

                #  for_002
                #  Pega todos os cpf registrados e verifica com o informado pelo cliente
                for cpf_sistema_verifica in self.lista_cpf_cliente:
                    if cpf_sistema_verifica == cpf_cliente_reserva:
                        # Apos a confirmação. O CPF é colocado na variável para ser usado mais a frente
                        self.confirmado_cpf_no_cadastro = cpf_sistema_verifica
                        self.quebra_loop = True  # Se tudo esta certo, quebra-se o loop_03

                        # Da as boas vindas ao cliente
                        for valor in self.lista_dados_cliente:
                            if cpf_sistema_verifica == valor[0]:
                                nome_cliente = valor[1]
                        print(f'Bem vindo, {nome_cliente}!\n'
                              f'Você já pode fazer sua reservar')

                        # Quebra apenas o loop 'for_002' quando encontra o cpf do cliente
                        break
                    else:
                        # Caso não encontrar o cpf, ele colocar a variável como falso, quebrando o loop_03
                        print(f'Você digitou o CPF [{cpf_cliente_reserva}], mas não foi encontrado seu cadastro.')
                        sleep(1)
                        print('Faça um cadastro e volte para continuar reservando!')
                        aperte_enter()
                        self.quebra_loop = False

                if self.quebra_loop:  # Quebra o loop_03
                    print('Seu cadastro foi encontrado')
                    break
                else:
                    break

            while True:  # loop_04
                # Caso não encontre o CPF informado pelo cliente
                if not self.quebra_loop:  # Recebe a posição do for_002, se for falso. Quebra o loop_03. Final da fila, recebe o break
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
                entrada = str(input('Escolha uma Poltrona (999 para Confirmar): ').upper())

                try:
                    valor_linha = entrada[0]
                    valor_coluna = int(entrada[1])
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

                    # Verificar se o lugar está ocupado. Caso esteja, pede para reservar outro.
                    if cinema[valor_linha][valor_coluna] == '--':
                        print('Não é possível reservar essa poltrona, reserve outra poltrona')
                        sleep(0.5)
                    else:  # Se o lugar estiver livre. Marca o local com o simbolo.
                        self.inf_reserva.append(cinema[valor_linha][valor_coluna])
                        cinema[valor_linha][valor_coluna] = str('--').strip()
                except:
                    print('OS Dados que você informou estão incorretos!')

                # Vai jogar na variável os dados dos cliente e ser mostrado conforme a opção
                for dados_cliente in self.lista_dados_cliente:
                    if dados_cliente[0] == self.confirmado_cpf_no_cadastro:
                        cpf_reservado = dados_cliente[0]
                        nome_reservado = dados_cliente[1]
                        # idade_reservado = dados_cliente[2]
                        # email_reservado = dados_cliente[3]
                if entrada == '999':
                    if len(self.inf_reserva) == 0:
                        print('Nenhuma poltrona foi reservada!')
                        break
                    else:
                        self.lista_reserva_cliente = [cpf_reservado, nome_reservado]
                        for reservas in self.inf_reserva:
                            self.lista_reserva_cliente.append(reservas)
                        if len(self.inf_reserva) == 1:
                            print(self.linhas_aparencia)
                            print(f'{nome_reservado} \nVocê reservou a poltrona: '
                                  f'{self.inf_reserva} \n')
                            aperte_enter()
                        else:
                            print(self.linhas_aparencia)
                            print(f"{nome_reservado}\n"
                                  f"Você reservou as seguintes poltronas ==> {self.inf_reserva}")
                            registro_da_reserva()
                            aperte_enter()
                            break

        # Iniciando o programa do zero
        cinema = sala_cinema()

        # Menu principal

        while True:
            data_menu = datetime.now()
            data_atual_menu = data_menu.strftime('%D/%M/%Y')
            hora_atual_menu = data_menu.strftime('%H:%M:%S')
            print(
                f'''
        Hora certa: 
        {data_atual_menu} - {hora_atual_menu}
        {self.linhas_aparencia}
        [1] Reservar uma Poltrona
        [2] Cadastrar um usuário
        [3] Veja suas reservas
        [0] Sair
        {self.linhas_aparencia} ''')
            resp_menu_principal = leiaInt('        Escolha uma opção: ')
            if resp_menu_principal == 1:
                reservar_cadeira()
            elif resp_menu_principal == 2:
                cadastro_cliente()
            elif resp_menu_principal == 3:
                consultar_registro_reserva()
            elif resp_menu_principal == 0:
                print('Fechando o programa')
                sleep(1)
                break
            else:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
