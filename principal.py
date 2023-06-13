import threading
from datetime import datetime
from time import sleep

# from threading import Thread

data = datetime.now()
ano_atual = data.strftime('%Y')
data_atual = data.strftime('%d/%m/%Y')
hora_atual = data.strftime('%H:%M:%S')

ano_formatado_inicio = str(data_atual).replace('/', ',')
ano_formatado_meio = ano_formatado_inicio.split(',')
ano_formatado_fim = [ano_formatado_meio]
for valor_formatado in ano_formatado_fim:
    # dia = int(valor_formatado[0])
    # mes = int(valor_formatado[1])
    dia = 10
    mes = 12
    ano = int(valor_formatado[2])
#print(ano)
#if dia >= 8 and mes >= 11:
#    print(ano - 1982)
#else:
#    print(ano - 1982 - 1)

arq_cadastro_cliente_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADASTRO_CLIENTE.txt'
arq_cadastro_registro_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/REGISTRO_RESERVAS.txt'
arq_cadeiras_reservadas = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADEIRAS_RESERVADAS.txt'


class SalaCinema:
    def __init__(self):
        self.linhas_aparencia = '--' * 40
        self.quebra_loop = True
        self.verificacao_reservas = False
        self.info_reserva = None
        self.inf_reserva = list()
        self.lista_reserva_cliente = list()
        self.lista_cpf_cliente = list()
        self.lista_dados_cliente = list()

        def aperte_enter():
            """
            :return: Retorna uma entrada de teclado, para dar uma pausa até o usuário decidir continuar
            """
            input('Aperte ENTER para continuar!')

        def leiaInt(valor_int):  # Verificar se o valor digitado é 'numero inteiro'
            """
            Essa função é responsavel por verificar se a entrada que os usuários informarem é um "número inteiro"
            :param valor_int: Recebe o texto exibido para o usuário.
            :return: Se o valor, digitado pelo usuário, for um número inteiro, ele retorna o valor como correto. Mas,
            caso o valor não for um "número inteiro" a função pede para o usuário digitar o valor navamente.
            """
            while True:  # loop_01
                try:
                    valor_correto = int(input(valor_int))
                    return valor_correto
                except ValueError:
                    print('Valor incorreto. Digite novamente.')

        def sala_cinema():  # A montagem do programa
            """
            :param: "PRIMEIRA ESTRUTURA DE CADEIRAS", responsavel em criar a primeira estrutura de paoltronas. Quando a
            primeira poltrona for reservada, essa estrutura esperara até a próxima atração.

            :param: "verificação de estrutura" essa condição serva para saber qual estrutura deve ser aprensentada no
            início do programa. Caso não tenha nenhuma cadeira reservada, seja a primeira vez que abre o programa, é
            preciso criar uma estrutura nova. Apos a verificação der FALSA, passa a buscar as informações dentro
            do arquivo de texto.

            :return: RETURN_1, caso a verificação seja verdadeira, então ele encaminha a estrutura que já está
            sendo reservada.
            :return: RETURN_2, se a verificação for falsa, então ele cria a 'PRIMEIRA ESTRUTURA DE CADEIRAS'.
            """

            # PRIMEIRA ESTRUTURA DE CADEIRAS
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
            verif_estrutura_reserva()
            valor_verificacao = self.verificacao_reservas

            # Verificação de estrutura
            if self.verificacao_reservas:
                return self.cadeiras_cinema_reservado  # RETURN_1
            else:
                return cinema_sala  # RETURNO_2

        def inicio_verif_arq_reserva():
            """
            Função para testes de threding
            """
            sleep(0.1)
            if not verificando_arq_registro_reserva():
                print(self.linhas_aparencia)
                print('Estamos criando o arquivo para você')
                sleep(1)
                print('Aguarde...!!')
                sleep(2)
                criando_arq_registro_reserva()
                sleep(1)
                print('Pronto, conseguimos criar o arquivo.')
                sleep(1)
                print('Faça uma boa reserva!!')
                print(self.linhas_aparencia)

        def verif_estrutura_reserva():
            """
            :param: loop_01_verificação, visa em formatar a string adquirida pelo arquivo de texto.

            :param: Valor_sem_caracteres_especial: essa variavel recebe as informações sem os caracteres especiais; removendo os
            caracteres "[", "]", "'". Como as informações foram gravadas em um bloco de notes do windows, quando solicitadas
            elas vem com os caracteres, sem indenficar se é uma lista.

            :param: valor_formatado_inicio, essa variavel recebe as informações um pouco mais limpa. Como existem espaços,
            e o metodo "\n" precisar ser removido. Como você vêem utilizei o metodo "replace" que vai substituir os caracteres
            que não fazem parte do conteúdo e vai trocá-los por outros. Nessa caso eu removi a "," e deixei sem nada
            depois eu precisei trocar o "espeço pela vírgula ","

            :param: valor_formatado_fim: nessa variavel, vamos transformar as informações da variavel valor_formatado_inicio
            em uma lista; com o metodo "split" pegamos todas as informações que estão entre vírgulas "," assim conseguimos
             seperar as informações e colocá-las uma lista.

            :param: lista_valor_arq, após ajustar as informações para uma lista, vamos adicioná-las realmente a uma lista
            "lista_valor_arq". Nesta lista vamos colocar em cada loop do FOR uma fileira do cinema até completa o loop.
            Depois que todas as informações estiverem na lista, segue-se a próxima linha.

            :param: na próxima linha, "verificação_de_conteu_falso", sera feita uma verificação para saber se o arquivo possui informações. Sempre que
            for aberto pela primeira vez o programa, o correto é sempre estava sem informações, como ele vai reconhecer
            que não possui dados, ele vai retornar o objeto "self.verificacao_reserva" como FALSO.

            :param: na parte da "verificar_de_conteudo_verdadeiro", ele vai iterar as informações em listas seperados,
            conforme a fileira. Perceba que a lista "lista_valor_arq" esta sendo iterada em cada variavel.

            :param: "verificar_cadeiras_reservadas" esse loop serve para verificar em possui alguma poltrona reservada.
            Caso tenha alguma, as informações que será apresentada na tela, contera as cadeiras reservadas.

            :return:
            """
            global abrindo_arq_cadeiras_reservadas
            cadeiras_cinema_reservado = list()
            cont_verificacao = 0
            verificacao_reservas_cadeiras = list()
            lista_valor_arq = list()
            valor_arq = list()
            try:
                abrindo_arq_cadeiras_reservadas = open(arq_cadeiras_reservadas, 'r')
                valor_arq = abrindo_arq_cadeiras_reservadas
            except FileNotFoundError:
                criando_arq_cadeiras_reserva = open(arq_cadeiras_reservadas, 'w')
                criando_arq_cadeiras_reserva.close()
            for valor in valor_arq:  # Loop_01_verificação
                valor_sem_caracteres_especial = (valor.replace("'", '').replace('[', '').replace(']', ''))
                valor_formatado_inicio = valor_sem_caracteres_especial.replace('\n', '').replace(',', '').replace(' ',
                                                                                                                  ',')
                valor_formatado_fim = valor_formatado_inicio.split(',')
                lista_valor_arq.append(valor_formatado_fim)

            # Verificação_de_conteudo_falso
            if len(lista_valor_arq) == 0:
                self.verificacao_reservas = False

            # Verificação_de_conteudo_verdadeiro
            else:
                fileira_a = lista_valor_arq[0]
                fileira_b = lista_valor_arq[1]
                fileira_c = lista_valor_arq[2]
                fileira_d = lista_valor_arq[3]
                fileira_e = lista_valor_arq[4]
                fileira_f = lista_valor_arq[5]
                fileira_g = lista_valor_arq[6]
                fileira_h = lista_valor_arq[7]
                fileira_i = lista_valor_arq[8]
                fileira_j = lista_valor_arq[9]
                self.cadeiras_cinema_reservado = [fileira_a, fileira_b, fileira_c, fileira_d, fileira_e,
                                                  fileira_f, fileira_g, fileira_h, fileira_i, fileira_j]

                # verificar_cadeiras_reservadas
                while True:
                    fila_a = lista_valor_arq[cont_verificacao]
                    for valor in fila_a:
                        valor_1 = str(valor)
                        if valor == '--':
                            self.verificacao_reservas = True
                    cont_verificacao += 1
                    if cont_verificacao == 9:
                        break

        def verificar_arq_cadastro_cliente():
            """
            Realiza um leituro no caminho que contem o arquivo de texto, que contem o cadastro dos clientes.
            :return: Se o valor for verdade, envia um False para a função "criando_arq_cadastro_cliente"
            """
            try:
                verificacao = open(arq_cadastro_cliente_local, 'r')
            except:
                return False
            verificacao.close()

        def verificando_arq_registro_reserva():
            """
            Igual à função "verificar_arq_cadastro_cliente". Essa função é responsavel por verificar se existe o arquivo
            de texto "REGISTRO_RESERVAS.txt". Esse arquivo é responsavel por registrar todos os registros que os clientes
            fizer, caso ele não existe, automaticamente ele é criado quando o cliente faz uma reserva.
            :return: retorna o valor de falso para a função "criando_arq_registro_reserva".
            """
            try:
                verificacao_arq_reserva_txt = open(arq_cadastro_registro_local, 'r')
                verificacao_arq_reserva_txt.close()
                return True
            except:
                return False
                
        def criando_arq_cadastro_cliente():
            """
            Após receber a informação de que o arquivo não existe. Essa função cria o arquivo no caminho solicitado.
            :return: Cria o arquivo de texto "CADASTRO_CLIENTE.txt"
            """
            try:
                criando_arq_cliente = open(arq_cadastro_cliente_local, 'w')
            except:
                print(self.linhas_aparencia)
                print('Não foi possível criar um arquivo para guardar seus cadastros')
            else:
                print('Não se preocupe, irei criar um cadastro para você')
                sleep(2)
                print('Prontinho!!')
                sleep(1)
                print('Arquivo para cadastro foi criado!!')
                sleep(1)
                print('Realize seu cadastro e boa reserva!!')
                print(self.linhas_aparencia)
                sleep(1)
                criando_arq_cliente.close()

        def criando_arq_registro_reserva():
            """
            Após receber o valor FALSO da função "criando_arq_registro_reserva", ele ira criar o arquivo de
            texto "criando_arq_registro_reserva"
            :return: cria o arquivo de texto no local configurado pelo desenvolvedor.
            """
            try:
                criando_arq_registro_reserva_txt = open(arq_cadastro_registro_local, 'w')
            except:
                print(self.linhas_aparencia)
                print('Não foi possível criar o arquivo para registrar suas reservas')
                aperte_enter()
            else:
                criando_arq_registro_reserva_txt.close()

        def gravando_dados_arq_cliente_txt(cpf, nome, idade, email):
            """
            Essa função é responsavel por gravar as informações do cliente, criando um cadastro.
            :param cpf: retorna o número do CPF, composta por 11 digitos. Parametro responsavel para localizar o cliente,
            gerar nota fiscal, entre outros.

            :param nome: retorna o nome do cliente, composta por caracteres de strings.

            :param idade: retorna a idade do cliente, composta por número inteiro. Parametro responsavel para
            classificação indicativa do filme.

            :param email: retorna o e-mail do cliente, comporta por caracteres de strings. Parametro responsavel para
            enviar promoções, informar a reserva, etc.

            :return gravando_dados: Grava todas as informações dentro do arquivo de texto "CADASTRO_CLIENTE.txt"
            """
            try:
                gravando_dados = open(arq_cadastro_cliente_local, 'a')
                gravando_dados.write(f'{cpf};{nome};{idade};{email}\n')
                print(self.linhas_aparencia)
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
            Quando cliente realiza uma reserva, as informações como, nome e cpf do cliente são gravadas com
            as cadeiras que foram solicitadas.
            :param: valor_1: recebe o valor iterado da lista de cadeiras, reservadas pelo cliente.
            :param: “cont”: contador, responsável em buscar as informações iteradas na lista. Ex cont = 1 - lista[cont] = lista[1]
            :param: gravando_reserva: salva os dados no arquivo de texto "REGISTRO_RESERVAS.txt".
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
                print(self.linhas_aparencia)
                print('Seu reserva foi concluída!')
                sleep(2)
                gravando_reserva.close()
            except:
                print('Não foi possível abrir o arquivo de texto para salvar sua reserva!')

        def lendo_dados_arq_cliente_txt():
            """
            Esta função é responsavel na leitura do arquivo de texto "CADASTRO_CLIENTE.txt", que contem os cadastro dso clientes.
            :return: A função sempre retorna dois objetos; self.lista_cpf_cliente e self.lista_dados_cliente.
                >> :param: self.lista.cpf_cliente: possui apenas a informação do CPF do cliente; ele é geralmente utilizada na função
                'reserva_cadeiras'
                >> :param: self.lista_dados_cliente: variável recebe todas as informações do cadastro do cliente e utiliza em diversas
            partes do programas
            """
            try:
                leitura = open(arq_cadastro_cliente_local, 'r')
            except:
                print(self.linhas_aparencia)
                print('-Erro ao abrir o arquivo de cadastro\n'
                      '-Arquivo pode estar corrompido ou...\n'
                      '-Arquivo não existe')
                print(self.linhas_aparencia)
                sleep(1)
                if not verificar_arq_cadastro_cliente():
                    criando_arq_cadastro_cliente()
            else:
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
            """
            Função responsavel em realizar a leitura das informações de reserva.
            :param leitura: Apos a função "gravando_reserva_cliente_txt" gravar as informações, depois da reserva,
            é possivel verificar quem realizou as reservas. Juntos, mais para frente, quando um cliente solicitar uma
            cadeira já reservada, aparecera as informações de quem realizou a reserva, caso não seja a mesma pessoa
            que fez a reserva, uma negação aparecerá na tela, informando que os dados são confidenciais.
            :return: Apos as informações serem lidas pela função, as informações eram inseridas no objeto
            lista "self.lista_info_registro"
            """
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

        def consultar_cadastro_cliente():
            """
            :param lendo_dados_arq_cliente_txt(): Quando chama a função "consultar_cadastro_cliente", ela vai primeiro
            buscar as informações. Apos a informações serem adicionadas na lista "self.lista_dados_cliente", as
            informações serão destribuidas no dicionário "self.dados_cliente_dict"

            :return: depois das informações coletadas, os dados é impresso para o usuário.
            """
            for valor_consulta in self.lista_dados_cliente:
                print(f'\n{self.linhas_aparencia}')
                self.dados_cliente_dict = {'Nome:': valor_consulta[1],
                                           'CPF:': valor_consulta[0],
                                           'Idade:': valor_consulta[2],
                                           'E-mail:': valor_consulta[3]}
                for chave, valor in self.dados_cliente_dict.items():
                    print(f'{chave} {valor}')
            self.linhas_aparencia
            aperte_enter()

        def consultar_registro_reserva():
            """
            Esta função ira mostrar as informações das reservadas feitas. Por enquanto ficar sincronizado com o arquivo
            "CADEIRAS_RESERVADAS.txt", pois conforme as cadeiras estiverem reservadas, ninguem mais poderá reservar.
            Em breve, irei adicionar uma função com os historicos de reservadas.

            :param: lendo_dados_no_arq_reserva: buscas as informações na função de mesmo nome. Coloca na variável
            "self.lista_inf_registro".
            :param: Self.lista_registro: objeto que possui informações sobre os dados das reservas.
            :param: valor_bruto: Pega todas as informações das várias "self.lista_info_registro" e distribui nos variáveis.
            :param: valor_limpo: responsável por separar as informações corretas e transferir para as variáveis referentes.
            :param: valor_limpo_cpf: vai receber apenas os dados de CFP do cliente. O CFP sempre sera iterado na posição 0.
            :param: valor_limpo_nome: recebe apenas os dados de Nome do cliente, o nome sempre sera iterado na posição 1.
            :param: cadeiras_reservadas: mostra todas as cadeiras reservadas pelo cliente. Como as cadeiras ficam no
            meio da lista é preciso "fatiar" usando as posições de 'cpf e nome, que fica no começo da lista' e
            'data e hora que fica no final da lista.'
            :param: data_reserva: pega as informações do dia, mes e ano, realizado a reserva.
            :param: hora_reserva: o mesmo que 'data_reserva', muda apenas a hora. Preferi deixar separado para poder
            manipular melhoras as informações.
            Existem momentos que eu preciso apenas da hora, assim como exite momentos que preciso apenas da data.
            :return: A função ira retornar de forma organizada as informações das reservas.
            """
            global valor_limpo, data_reserva, hora_reserva
            lendo_dados_no_arq_reserva()
            for valor_bruto in self.lista_info_registro:
                valor_limpo = valor_bruto.split(';')
                valor_limpo_cpf = valor_limpo[0]
                valor_limpo_nome = valor_limpo[1]
                cadeiras_reservadas = valor_limpo[2:-2]
                data_reserva = valor_limpo[-2]
                hora_reserva = valor_limpo[-1]
                print(f'\n{self.linhas_aparencia}')
                print(f'\nNome: {valor_limpo_nome} CPF: {valor_limpo_cpf}, você reservou {len(cadeiras_reservadas)} cadeiras')
                print('Cadeiras reservadas:', end='')
                for valor in cadeiras_reservadas:
                    print(f'[{valor}]', end=' ')
                print(f'\nReserva feita na data: {data_reserva} - {hora_reserva} \n{self.linhas_aparencia}')

        def cadastro_cliente():
            """
            Função responsavel por cadastrar os clientes. São quatro parametros que são solicitadoas. Mais para frente,
            serão solicitados mais informações, mas por hora são apenas esses.

            :param nome_cadastro: Variavel que recebera o nome completo do cliente. Com o nome, ficara mais fácil para
            indentificar o responsavel pela reserva.

            :param cpf_cadastro: Variavel vai receber o número de CPF do cliente, mais para frente vou colcoar mais restrições
            na hora do preenchimento, pois não pode ter "pontos" e nem o "troço" no final do cpf, mas considerarei
            esses parametros.

            :param idade_cadastro: A idade sera de extrema importancia nessa programa, pretendo usá-lo para classificar
            a indicação do filme por idade. Essa campo é obrigatorio preencher, ainda não coloquei os parametros de
            obrigação mais em breve irei adicionar.

            :param email_cadastro: o email, sera responsavel em encaminhar uma menssagem informando sobre a reserva feita

            :return: Quando as informações estiverem completas, os dados serão encaminhados para a função
            "gravando_dados_arq_cliente_txt"
            """
            while True:  # loop_02
                print(self.linhas_aparencia)
                nome_cadastro = input('Digite seu nome completo: ').title()
                cpf_cadastro = input('Digite seu CPF: ')
                idade_cadastro = leiaInt('Digite sua idade: ')
                email_cadastro = input('Digite seu e-mail: ')

                print(self.linhas_aparencia)
                print(f'Os dados que serão cadastrados são: \n\n'
                      f'Nome: {nome_cadastro}\n'
                      f'CPF: {cpf_cadastro}\n'
                      f'Idade: {idade_cadastro}\n'
                      f'Email: {email_cadastro}')
                print(self.linhas_aparencia)

                aperte_enter()
                gravando_dados_arq_cliente_txt(cpf_cadastro, nome_cadastro, idade_cadastro, email_cadastro)
                resp = input('Realizar outro cadastro? [S/N]: ').upper()
                if resp == 'N':
                    lendo_dados_arq_cliente_txt()
                    break

        # Corpo do programa
        def reservar_cadeira():
            """
            :param: 'lendo_dados_arq_cliente_txt' é preciso ativar a função para as variáveis serem preenchidas com os dados.
            :param: 'cinema' variável que recebe as informações para estruturar a sala de cinema; 'sala_cinema()' busca as
            informações nas listas internas e joga na variável 'cinema'.
            :return:
            """
            global valor_linha, valor_coluna, nome_cliente, nome_reservado, cpf_reservado, cpf_sistema_verifica
            cpf_confirma = False

            while True:  # loop_03
                # Inicia a verificação do cadastro.
                self.quebra_loop = True
                print(self.linhas_aparencia)
                print('Preciso que entre com o seu CPF para que possemos reservar uma poltrona.')
                cpf_cliente_reserva = leiaInt('Digite seu CPF: ')
                print(self.linhas_aparencia)
                print('Verificando o bando de dados...!')
                print(self.linhas_aparencia)

                # CASO NÃO EXISTE NENHUM CADASTRO, PROGRAMA NÃO CONTINUA
                if len(self.lista_cpf_cliente) == 0:
                    sleep(2)
                    print('- DESCULPE!!! '
                          '- Não encontramos nenhum registro no sistema. \n'
                          '- Verifique se o banco de dados esta tudo certinho! \n'
                          '- Caso o banco de dados esteja funcionando normalmente, verifique se você possui cadastro!')
                    print(self.linhas_aparencia)
                    aperte_enter()
                    self.quebra_loop = False
                    break
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
                    sleep(1)
                    print('Encontramos seu cadastro... !', end='')  # Avisa que encontro o cadastro
                    sleep(1)
                    print(f'Seja bem vindo Sr/a {nome_cliente}')  # Da as boas vindas para o cliente, pelo nome.
                    self.linhas_aparencia
                    aperte_enter()
                else:  # Caso não encontre o cadastro, vai pedir para voltar no meu principal
                    sleep(1)
                    print(self.linhas_aparencia)
                    print(f'O cadastro com o CPF:{cpf_cliente_reserva}, não foi encontrado!!\n'
                          f'Caso ainda não tenha feito um cadastro, sugerimos que crie um no menu principal')
                    print(self.linhas_aparencia)
                    aperte_enter()
                    self.quebra_loop = False

                if self.quebra_loop:  # Quebra o loop_03
                    break
                else:
                    break

            while True:  # loop_04
                # Caso não encontre o CPF informado pelo cliente
                if not self.quebra_loop:  # Recebe a posição do for_002, se for falso. Quebra o loop_03. Final da fila, recebe o break.
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
                        print()
                        print('Essa poltrona já foi reservada, reserve outra poltrona')
                        print(self.linhas_aparencia)
                        aperte_enter()
                        print()
                    else:  # Se o lugar estiver livre. Marca o local com o simbolo.
                        self.inf_reserva.append(cinema[valor_linha][valor_coluna])
                        cinema[valor_linha][valor_coluna] = str('--').strip()
                except TypeError:
                    print('Opção incorreta!')

                # Vai jogar na variável os dados dos cliente e ser mostrado conforme a opção
                for dados_cliente in self.lista_dados_cliente:
                    if dados_cliente[0] == self.confirmado_cpf_no_cadastro:
                        cpf_reservado = dados_cliente[0]
                        nome_reservado = dados_cliente[1]

                if entrada == '999':
                    if len(self.inf_reserva) == 0:
                        print('Nenhuma paltrona foi reservada!')
                        print(self.linhas_aparencia)
                        aperte_enter()
                        break
                    else:
                        if len(self.inf_reserva) == 1:
                            print(f'Sr(a). {nome_reservado} \n'
                                  f'Você reservou a poltrona: '
                                  f'{self.inf_reserva} \n')
                            print(self.linhas_aparencia)
                            gravando_reserva_cliente_txt(nome_reservado, cpf_reservado)
                            aperte_enter()
                            self.cadeiras_reservadas = cinema
                            atualizando_estrutura_cinema()
                            break
                        else:
                            print(f"Sr(a). {nome_reservado}\n"
                                  f"Você reservou as seguintes poltronas ==> {self.inf_reserva}")
                            gravando_reserva_cliente_txt(nome_reservado, cpf_reservado)
                            print(self.linhas_aparencia)
                            aperte_enter()
                            self.cadeiras_reservadas = cinema
                            atualizando_estrutura_cinema()
                            break

        """
        Vejas as linhas abaixo do texto.
        :param cinema: Pega as informações na função "sala_cinema" para criar a estrutura que o usuário ira visualizar.
        :param lendo_dados_arq_cliente_txt: Quando o programa abrir, ele vai pegar as informações do cliente no banco de 
        dados e deixa-lo disponivel para o sistema utilizar conforme necessidade. 
        :param lendo_dados_no_arq_reserva: Depois que as informações do cliente estiverem disponivel, sera preciso colocar
        as informações de reservas, como, nome e cpf do cliente que reservou, quais as cadeiras reservadas, etc. Essas 
        informações serão necessarias para saber quem reservou as cadeiras.
        """
        cinema = sala_cinema()
        lendo_dados_arq_cliente_txt()
        lendo_dados_no_arq_reserva()

        def atualizando_estrutura_cinema():
            """
            :param: gravando_arq_reserva_restrutura. É responsavel por registrar as cadeiras que foram reservadas.
            Quando programa é fechado, as informações são retiradas da memória, então é precisa um registro em um
            arquivo de texto, que fica localizado no computador.
            :return:
            """
            gravando_arq_reserva_restrutura = open(arq_cadeiras_reservadas, 'w')
            for valor_reservas in self.cadeiras_reservadas:
                valor_formatado = str(valor_reservas).strip()
                gravando_arq_reserva_restrutura.write(f'{valor_reservas}\n')
            gravando_arq_reserva_restrutura.close()

        # Menu principal
        while True:
            data_menu = datetime.now()
            data_atual_menu = data_menu.strftime('%d/%m/%y')
            hora_atual_menu = data_menu.strftime('%H:%M:%S')
            print(
                f'''
                      Hora certa
        |                                     |
        |         {data_atual_menu} - {hora_atual_menu}         |
        |_____________________________________|
        {self.linhas_aparencia}
        |[1]| => Reservar uma Poltrona        
        |[2]| ==> Cadastrar um usuário
        |[3]| ===> Consultar Cadastro de cliente
        |[4]| ====> Veja suas reservas
        |[0]| =====> Sair
        {self.linhas_aparencia} ''')
            resp_menu_principal = leiaInt('        Escolha uma opção: ')

            # OPÇÃO RESERVAR CADEIRAS
            if resp_menu_principal == 1:
                reservar_cadeira()

            # OPÇÃO CADASTRAR CLIENTE
            elif resp_menu_principal == 2:
                cadastro_cliente()

            # OPÇÃO CONSULTAR CADASTRO CLIENTE
            elif resp_menu_principal == 3:
                if len(self.lista_dados_cliente) == 0:
                    print(self.linhas_aparencia)
                    print('-Não existe nenhum cliente cadastrado')
                    print('-Volta ao menu principal e escolha a opção "2" para realizar um cadastro.')
                    print(self.linhas_aparencia)
                    aperte_enter()
                else:
                    consultar_cadastro_cliente()
            # OPÇÃO REGISTRO RESERVA
            elif resp_menu_principal == 4:
                consultar_registro_reserva()
                if len(self.lista_info_registro) == 0:
                    print(self.linhas_aparencia)
                    print('Não encontrei nenhum registro no sistema. '
                          'Verifique se a sessão já terminou...')
                    aperte_enter()
            # OPÇÃO SAIR
            elif resp_menu_principal == 0:
                print(self.linhas_aparencia)
                print('Fechando o programa')
                sleep(1)
                break
            else:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
