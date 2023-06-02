import threading
from time import sleep
from datetime import datetime

# from threading import Thread

data = datetime.now()
ano_atual = data.strftime('%y')
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
        self.lista_cpf_cliente = list()
        self.lista_dados_cliente = list()

        def aperte_enter():
            """
            :return: Retorna uma entrada de teclado, para dar uma pausa até o usuário decidir continuar
            """
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
        def gravando_dados_arq_cliente_txt(cpf, nome, idade, email):
            """
            :param cpf:
            :param nome:
            :param idade:
            :param email:
            """
            try:
                gravando_dados = open(arq_cadastro_cliente_local, 'a')
                gravando_dados.write(f'{cpf};{nome};{idade};{email}\n')
                print('Cadastro realizado com sucesso!!')
                sleep(1)
            except:
                print('Não foi possível cadastrar seu usuário')
                if not verificando_arq_registro_reserva():
                    criando_arq_registro_reserva()
            else:
                gravando_dados.close()

        def gravando_reserva_cliente_txt(nome_reserva, cpf_reserva):
            """
            :param valor_1: Recebe o valor iterado da lista de cadeiras
            :param cont: Contador, resposabel em buscar as informações iteradas na lista. Ex cont = 1 - lista[cont] = lista[1]
            :param gravando_reserva: Salva os dados em um arquivo txt
            """
            try:
                gravando_reserva = open(arq_cadastro_registro_local, 'a')
                gravando_reserva.write(f'{cpf_reserva};{nome_reserva};')
                cont = 0
                while True:
                    valor_1 = self.inf_reserva[cont]
                    cont += 1
                    gravando_reserva.write(f'{valor_1};')
                    if cont == len(self.inf_reserva):
                        break
                gravando_reserva.write(f'{data_atual};{hora_atual}\n')
                print('Seu reserva foi concluida!')
                sleep(2)
                gravando_reserva.close()
            except:
                print('Não foi possível abrir o arquivo de texto para salvar sua reserva!')

        def lendo_dados_arq_cliente_txt():
            # Variáveis locais
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
                for valor_bruto in leitura:
                    valor_limpo = valor_bruto.strip()
                    self.lista_info_registro.append(valor_limpo)
                if len(self.lista_info_registro) == 0:
                    print(self.linhas_aparencia)
                    print('Não encontrei nenhum registro no sistema. '
                          'Verifique se a sessão já terminou')
                    aperte_enter()

        def consultar_cadastro_cliente():
            lendo_dados_arq_cliente_txt()
            for valor_consulta in self.lista_dados_cliente:
                self.dados_cliente_dict = {'Nome:': valor_consulta[1],
                                           'CPF:': valor_consulta[0],
                                           'Idade:': valor_consulta[2],
                                           'E-mail:': valor_consulta[3]}
                for chave, valor in self.dados_cliente_dict.items():
                    print(f'{chave} {valor}')
            aperte_enter()

        # Manipulações
        def cadastro_cliente():
            while True:  # loop_02
                nome_cadastro = input('Digite seu nome completo: ').title()
                cpf_cadastro = input('Digite seu CPF: ')
                idade_cadastro = leiaInt('Digite sua idade: ')
                email_cadastro = input('Digite seu e-mail: ')

                print(f'Os dados que serão cadastrados são: \n'
                      f'Nome: {nome_cadastro}\n'
                      f'CPF: {cpf_cadastro}\n'
                      f'Idade: {idade_cadastro}\n'
                      f'Email: {email_cadastro}\n')
                aperte_enter()
                gravando_dados_arq_cliente_txt(cpf_cadastro, nome_cadastro, idade_cadastro, email_cadastro)
                resp = input('Continuar cadastrando? [S/N]: ').upper()
                if resp == 'N':
                    break

        # Verificar o arq que contem os registros de reservas
        def consultar_registro_reserva():
            global valor_limpo
            cont = -10
            lendo_dados_no_arq_reserva()
            for valor_bruto in self.lista_info_registro:
                valor_limpo = valor_bruto.split(';')
                valor_limpo_cpf = valor_limpo[0]
                valor_limpo_nome = valor_limpo[1]
                cadeiras_reservadas = valor_limpo[2:-2]
                data_reserva = valor_limpo[-1]
                hora_reserva = valor_limpo[-2]
                print()
                print(f'\n{self.linhas_aparencia}')
                print(
                    f'\nNome: {valor_limpo_nome} CPF: {valor_limpo_cpf}, você reservou {len(cadeiras_reservadas)} cadeiras')
                print('Cadeiras reservadas:', end='')
                for valor in cadeiras_reservadas:
                    print(f'[{valor}]', end=' ')
            print(f'\nReserva feita na data: {data_reserva} - {hora_reserva} \n{self.linhas_aparencia}')

        # Corpo do programa
        def reservar_cadeira():
            self.add_registro_reserva = list()
            global valor_linha, valor_coluna, nome_cliente, nome_reservado, cpf_reservado, cpf_sistema_verifica
            cpf_confirma = False
            lendo_dados_arq_cliente_txt()
            # dados_cliente_confirmado = dict()
            while True:  # loop_03

                # Inicia a verificação do cadastro.
                self.quebra_loop = True
                print(self.linhas_aparencia)
                print('Preciso que entre com o seu CPF para que possemos reservar uma poltrona.')
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
                    if cpf_cliente_reserva == cpf_sistema_verifica:  # Se o CPF foi encontrado...
                        self.confirmado_cpf_no_cadastro = cpf_cliente_reserva
                        cpf_confirma = True  # Deixa a variável VERDADEIRA depois que encontra o CPF
                        for valor_nome in self.lista_dados_cliente:  # Vai colocar o nome do cliente, conforme o cpf
                            if cpf_sistema_verifica == valor_nome[0]: \
                                    # Busco na lista de cadastro o nome referente ao cpf
                                nome_cliente = valor_nome[1]  # após encontrar, joga na variável
                if cpf_confirma:  # Se a busca pelo CPF foi verdadeira...
                    self.linhas_aparencia
                    print('Verificando o banco de dados, aguarde...!')
                    sleep(1)
                    print('Encontramos seu cadastro!')  # Avisa que encontro o cadastro
                    sleep(0.5)
                    print(f'Seja bem vindo Sr/a {nome_cliente}')  # Da as boas vindas para o cliente, pelo nome.
                    self.linhas_aparencia
                    print('Boa reservar!')
                    aperte_enter()
                else:  # Caso não encontre o cadastro, vai pedir para voltar no meu principal
                    sleep(0.5)
                    self.linhas_aparencia
                    print(f'O cadastro com o CPF:{cpf_cliente_reserva}, não foi encontrado!!\n'
                          f'Caso ainda não tenha feito um cadastro, sugerimos que crie um no menu principal')
                    self.linhas_aparencia
                    aperte_enter()
                    self.quebra_loop = False

                if self.quebra_loop:  # Quebra o loop_03
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
                if entrada == '999':
                    if len(self.inf_reserva) == 0:
                        print('Nenhuma poltrona foi reservada!')
                        break
                    else:
                        if len(self.inf_reserva) == 1:
                            print(self.linhas_aparencia)
                            print(f'Sr(a). {nome_reservado} \n'
                                  f'Você reservou a poltrona: '
                                  f'{self.inf_reserva} \n')
                            gravando_reserva_cliente_txt(nome_reservado, cpf_reservado)
                            aperte_enter()
                            break
                        else:
                            print(self.linhas_aparencia)
                            print(f"Sr(a). {nome_reservado}\n"
                                  f"Você reservou as seguintes poltronas ==> {self.inf_reserva}")
                            gravando_reserva_cliente_txt(nome_reservado, cpf_reservado)
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
        [1] => Reservar uma Poltrona        
        [2] ==> Cadastrar um usuário
        [3] ===> Consultar Cadastro de cliente
        [4] ====> Veja suas reservas
        [0] =====> Sair
        {self.linhas_aparencia} ''')
            resp_menu_principal = leiaInt('        Escolha uma opção: ')
            if resp_menu_principal == 1:
                reservar_cadeira()
            elif resp_menu_principal == 2:
                cadastro_cliente()
            elif resp_menu_principal == 3:
                consultar_cadastro_cliente()
                self.dados_cliente_dict.clear()
            elif resp_menu_principal == 4:
                consultar_registro_reserva()
            elif resp_menu_principal == 0:
                print('Fechando o programa')
                sleep(1)
                break
            else:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
