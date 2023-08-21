import threading
from datetime import datetime
from time import sleep
from os import listdir, remove

arq_cadastro_cliente_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADASTRO_CLIENTE.txt'
arq_cadastro_registro_local = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/REGISTRO_RESERVAS.txt'
arq_cadeiras_reservadas = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/CADEIRAS_RESERVADAS.txt'
arq_cadastro_filmes_local_txt = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/FILMES_CADASTRADOS.txt'
arq_filmes_em_cartazes_local_pasta = 'G:/Meu Drive/Estudos/Python/Arquivos de texto/SALA_CINEMA/FILMES_EM_CARTAZES'


class SalaCinema:
    def __init__(self):
        self.linhas_aparencia = '--' * 40
        self.quebra_loop = True
        self.verificacao_reservas = False
        self.info_reserva = None
        self.inf_reserva = list()
        self.lista_cpf_cliente = list()
        self.lista_dados_cliente = list()
        self.lista_de_filmes_cadastrados = list()
        self.lista_filme_cadastrado = list()
        self.lista_info_registro = list()
        self.registros_filmes = list()
        
        def func_qtdd_cadeiras():
            """
            Essafuncação vai ser destinada a escolher a quantidade de cadeiras que serão disponibilizadas para cada filmes. 
            Quando foi colocar o filme em cartz, o program chama essa funcao e é escolho quantas fileiras e cadeiras. 
            Função essa que ajuda me ajudar com a monipulação de matrizes.
            :return: 
            """

        def func_data_atual():
            valor_data = datetime.now()
            self.data_atual = valor_data.strftime('%d/%m/%Y')
            self.hora_atual = valor_data.strftime('%H:%M:%S')

        def mes_extenso(valor_data):
            global mes
            valor_data_num = str(valor_data[0])
            if valor_data_num == '0':
                mes = int(valor_data[1]) - 1
            elif valor_data_num == '1':
                mes = int(valor_data_num) - 1
            lista_mes = ['Janeiro', 'Fevereiro', 'Março',
                         'Abril', 'Maio', 'Junho',
                         'Julho', 'Agosto', 'Setembro',
                         'Outubro', 'Novembro', 'Desembro']
            return lista_mes[mes]

        def func_logo_cinema(texto_exibicao):
            print(self.linhas_aparencia)
            print(f'{texto_exibicao}'.center(80))
            print(self.linhas_aparencia)

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

        def func_verificar_data_cartaz():
            """
            O intuito dessa função é verificar se os filmes que estão em cartaz ainda estão no periodo. Caso
            esteja chegando no final ou já terminado, o filme é retirado de cartaz e as informações ficara dentro
            de um arquivo de log para registro. Assim, quando o cliente abrir o programa, evita que ele encontre
            o filme na lista, sendo que já passou a data. O arquivo de log vai server para, caso o cliente consiga
            encontrar as informações do filme, mostra quando ele entrou em cartaz e saiu.
            :return:
            """
            func_data_atual()

            data_atual = str(self.data_atual).split('/')
            dia_atual = data_atual[0].strip()
            mes_atual = data_atual[1].strip()
            ano_atual = data_atual[2].strip()
            mes_atual_extenso = mes_extenso(mes_atual)
            print()
            print(f'Data Atual [{dia_atual} de {mes_atual_extenso} de {ano_atual}]')
            func_logo_cinema("Filmes em cartaz, Aproveite!!")
            listando_filmes_cartaz = listdir(arq_filmes_em_cartazes_local_pasta)
            for valor_busca in listando_filmes_cartaz:
                filme_cartaz_formt = valor_busca.split('-')
                filme_cartaz_data = filme_cartaz_formt[1].replace('_', '/').replace('(', '').replace(')', '').strip()
                data_termino_cartaz = filme_cartaz_data.split('/')
                # filme_termino_cartaz = listando_filmes_cartaz[2].replace('.txt', '')
                ano_termino = data_termino_cartaz[2].strip()
                mes_termino = data_termino_cartaz[1].strip()
                dia_termino = data_termino_cartaz[0].strip()
                mes_termino_extenso = mes_extenso(mes_termino)
                data_termino = f'{dia_termino}/{mes_termino}/{ano_termino}'
                if ano_termino < ano_atual:
                    print(f"O ano de terminio é {ano_termino}, foi no ana passado - Filmes foi removido das salas")
                    remove(arq_filmes_em_cartazes_local_pasta + '/' + valor_busca)
                elif ano_termino == ano_atual:
                    if mes_termino < mes_atual:
                        print(f'O mes {mes_termino_extenso} terminou, o filme estava em cartaz até o dia {data_termino}\n'
                              f'Filme {valor_busca} foi removido das salas!')
                        remove(arq_filmes_em_cartazes_local_pasta + '/' + valor_busca)
                    elif mes_termino == mes_atual:
                        if dia_termino < dia_atual:
                            print(f'{valor_busca} filmes esta sendo removido das salas de cinema!')
                            remove(arq_filmes_em_cartazes_local_pasta + '/' + valor_busca)
                        elif dia_termino == dia_atual:
                            print(f'{valor_busca} esta em seu ultimo dia!!')
                        else:
                            print(f'{valor_busca} esta em seu ultimo mes, vai sair das salas de cinam no dia '
                                  f'{dia_termino} de {mes_atual_extenso}')
                    elif mes_termino > mes_atual:
                        print(f'Filme {valor_busca} vai esta em cartaz até {data_termino}')
                elif ano_termino > ano_atual:
                    print(f'Filmes {valor_busca} ira ficar em cartaz até o dia {dia_termino}/{mes_termino}/{ano_termino}')
                print(self.linhas_aparencia)

        def calculando_data():
            """
            O objetivo dessa função é aprender a mudança do mes, dependendo do dia que for acrescido, tipo:
            O mesmo possui 30 dias, vou colocar um filme de cartaz para ficar 25 dias nas salas de cinema, mas
            quando eu for registrar o filme é dia 25-07-2023. Quando eu for registrar o filme sera pedido o periodo
            em dias, em 7 dias já sera o próximo mes, agosto, mas com o cálculo que fiz, ele apenas vai somar
            os dias 25 + 25 tormando-se 50-07-2023.
            Essa função eu vou usar para fazer essa culculo, facilitando na hora do registro.
            Vou tentar fazer sem ajudar da foruns, tentar resolver sozinho, para assim tentar entender o funcionamento.
            :return:
            """

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
                print('Faça uma boa reserva!')
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

            :param: na próxima linha, "verificação_de_conteu_falso", sera feita uma verificação para saber se o arquivo
            possui informações. Sempre que for aberto pela primeira vez o programa, o correto é sempre estava sem
            informações, como ele vai reconhecer que não possui dados, ele vai retornar o objeto
            "self.verificacao_reserva" como FALSO.

            :param: na parte da "verificar_de_conteudo_verdadeiro", ele vai iterar as informações em listas seperados,
            conforme a fileira. Perceba que a lista "lista_valor_arq" esta sendo iterada em cada variavel.

            :param: "verificar_cadeiras_reservadas" esse loop serve para verificar em possui alguma poltrona reservada.
            Caso tenha alguma, as informações que será apresentada na tela, contera as cadeiras reservadas.

            :param self.verificacao_reservas: Quando o valor da reserva for VERDADEIRO, significa que existe uma cadeira
            reserva, então ele precisa carregar a estrutura já configurada com a reserva.

            :return:
            """
            global abrindo_arq_cadeiras_reservadas
            cont_verificacao = 0
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

        def func_listando_filmes_cartaz():
            """
            Função destinadas em lista os filmes que estiverem em cartaz.
            :return:
            """
            func_data_atual()
            filmes_listados = listdir(arq_filmes_em_cartazes_local_pasta)
            if len(filmes_listados) == 0:
                print('Não encontrei nenhum filme em cartaz!')
            else:
                for filmes in filmes_listados:
                    valor_form_filme_01 = filmes.replace('.txt', '')
                    valor_form_filme_02 = valor_form_filme_01.split('-')
                    valor_titulo_listando = valor_form_filme_02[2]
                    valor_data_listando = valor_form_filme_02[1].replace('_', '/').replace('(', '').replace(')', '')
                    print(self.linhas_aparencia)
                    lista = filmes.split('-')
                    data_termino_formatado = lista[1].replace('_', '/').replace('(', '').replace(')', '').strip()
                    fim_cartaz = data_termino_formatado
                    if self.data_atual == fim_cartaz:
                        print(f'O filme [{valor_form_filme_01}] está em seu ultimo dia!')
                    elif self.data_atual > fim_cartaz:
                        remove(str(arq_filmes_em_cartazes_local_pasta + '/' + filmes))
                        print(f'Filme [{valor_form_filme_01}] saiu de cartaz!!')
                    else:
                        print(f'O filme [{valor_titulo_listando}] ficara em cartaz até o dia {valor_data_listando}')
            print(self.linhas_aparencia)
            aperte_enter()    

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
                print('Realize seu cadastro e boa reserva!')
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
                gravando_reserva.write(f'{self.data_atual};{self.hora_atual}\n')
                self.inf_reserva.clear()
                print(self.linhas_aparencia)
                print('Seu reserva foi concluída!')
                sleep(2)
                gravando_reserva.close()
            except:
                print('Não foi possível abrir o arquivo de texto para salvar sua reserva!')

        def gravando_filmes_em_cartaz():
            """
            Area destinada a gravar os filmes que ficaram em cartaz.
            :param: func_data_atual() atualiza no sistema a data atual, coloca no objeto self.data_atual
            :param: lendo_dados_no_arq-filmes_txt() atualiza as informações dos filmes que estão no cadastrados, as
            informações são gravadas no obejto "self.lista_filmes_cadastrado"
            :param: loop_listando_filmes_cadastrados:
            :param: loop_lista_verifica_filmes_cartaz: esse loop é responsavel por analisar se o filme esta em cartaz.
            O programa lista a pasta responsavel e caso encontre o codigo do filme na pasta, o objeto self.'quebra_loop'
            passa a ter o valor 'True' e quabra do loop loop_cadastrando_filme_cartaz. Caso o filme não estaje na lista
            o objeto self.'quebra_loop' passa a ter o valor 'False' e continuar o cadastro.

            :param: loop_registro_filme_cartaz:
            obs: Verificar duplicidade no registro dos filmes

            :return:
            """
            global cod_filme
            func_data_atual()
            lendo_dados_no_arq_filmes_txt()

            # loop_listando_filmes_cadastrados
            for lista_filmes in self.lista_filme_cadastrado:
                print(self.linhas_aparencia)
                print(
                    f'Registro: {lista_filmes[0]} \n'
                    f'Titulo: {lista_filmes[1]} \n'
                    f'Genero: {lista_filmes[2]} \n'
                    f'Duração: {lista_filmes[3]} minutos \n'
                    f'Classificação: {lista_filmes[4]} \n'
                    f'Sinopse:')
                for valor_sinopse in lista_filmes[5]:
                    if valor_sinopse != '.':
                        valor_str = str(valor_sinopse).title()
                        print(f'{valor_str}', end='')
                    else:
                        print(f'')
            print(self.linhas_aparencia)
            print()
            print('Digite o código do filme para reserva-lo!')
            valor_codigo_filme = leiaInt('Cod:')
            print(self.linhas_aparencia)
            valor_cod_formt = str(valor_codigo_filme)
            if len(valor_cod_formt) == 1:
                cod_filme = "0" + "0" + "0" + valor_cod_formt
            elif len(valor_cod_formt) == 2:
                cod_filme = '0' + '0' + valor_cod_formt
            elif len(valor_cod_formt) == 3:
                cod_filme = str('0' + valor_cod_formt)

            # loop_lista_verifica_filmes_cartaz
            print()
            print(f'Filmes em cartaz ')
            print(self.linhas_aparencia)
            listando_filmes_cartaz = listdir(arq_filmes_em_cartazes_local_pasta)
            for valor_listagem in listando_filmes_cartaz:
                valor_formt_list = valor_listagem.split('-')
                valor_cod_list_str = valor_formt_list[0].strip()
                valor_titulo_list_str = valor_formt_list[2].replace('.exe', '').strip()
                valor_data_list_str = valor_formt_list[1].replace('_', '/').strip()
                print(f'[{valor_cod_list_str}] - {valor_titulo_list_str}')
                if valor_cod_list_str == cod_filme:
                    print()
                    print(self.linhas_aparencia)
                    print(f"O filme que você digitou [{valor_titulo_list_str.replace('.txt', '')}] já esta em cartaz!\n"
                          f"Ficara até o dia {valor_data_list_str}")
                    print(self.linhas_aparencia)
                    # Se encontrou o filme em cartaz, quebra o loop_cadastrando_filme_cartaz
                    self.quebra_loop = False
                    aperte_enter()
                    break
                else:
                    # Se não encontrou, é verdadeiro.
                    self.quebra_loop = True

            # loop_cadastrando_filme_cartaz
            while True:
                if not self.quebra_loop:
                    break
                # loop_registro_filme_cartaz
                for codigo in self.lista_filme_cadastrado:
                    if int(cod_filme) == int(codigo[0]):
                        print()
                        print(f'Você vai coloca em cartaz o filme...:\n'
                              f'Titulo:[{codigo[1]}], com duração de: [{codigo[3]}] minutos')
                        valor_fim_cartaz = input('Até que dia o filme ficara em cartaz? (dd/mm/aaaa): ')
                        data_fim_cartaz = str(valor_fim_cartaz).replace('/','_')
                        arq_filme_txt = str('/' + codigo[0] + ' - ' + '(' + data_fim_cartaz + ')' + ' - ' \
                                            + codigo[1] + '.txt')
                        try:
                            verif_arq_cartaz = open(arq_filmes_em_cartazes_local_pasta + arq_filme_txt, 'r')
                            print()
                            print(f'O filme [{codigo[1]}] vai ficar em cartaz até [{valor_fim_cartaz}]')
                            print('Para continuar...')
                            aperte_enter()
                            verif_arq_cartaz.close()

                        except FileNotFoundError:
                            print('Registrando filme... aguarde!')
                            print()
                            sleep(2)
                            try:
                                gravando_filme_cartaz = open(arq_filmes_em_cartazes_local_pasta + arq_filme_txt, 'w')
                                data_inicio_cartaz = str(self.data_atual)
                                gravando_filme_cartaz.write(f'{codigo[1]};{codigo[3]};'
                                                            f'{data_inicio_cartaz};'
                                                            f'{data_fim_cartaz} \n')
                                sleep(1)
                                print('Filme registrado com sucesso!!')
                                self.quebra_loop = False
                                break
                            except:
                                sleep(2)
                                print(f'Não foi possível criar o arquivo para o filme [{codigo[1]}]')
                                print('Analise o codigo')
                                print(self.linhas_aparencia)
                                aperte_enter()
                                break
                print(self.linhas_aparencia)
                aperte_enter()
                print()

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

        def lendo_dados_no_arq_filmes_txt():
            try:
                lendo_arq_cadastro_de_filmes = open(arq_cadastro_filmes_local_txt)
            except FileNotFoundError:
                print('Arquivo de texto não existe.')
            else:
                for valor_lendo_arq in lendo_arq_cadastro_de_filmes:
                    valor_arq_formatado = valor_lendo_arq.split(';')
                    lendo_dados_registro = valor_arq_formatado[0]
                    lendo_dados_titulo = valor_arq_formatado[1]
                    lendo_dados_genero = valor_arq_formatado[2]
                    lendo_dados_duracao = valor_arq_formatado[3]
                    lendo_dados_classificacao = valor_arq_formatado[4]
                    lendo_dados_sinopse = valor_arq_formatado[5]
                    self.lista_filme_cadastrado.append([lendo_dados_registro, lendo_dados_titulo, lendo_dados_genero,
                                                        lendo_dados_duracao, lendo_dados_classificacao,
                                                        lendo_dados_sinopse])
                    self.registros_filmes.append([lendo_dados_registro, lendo_dados_titulo])

        def consultar_cadastro_cliente():
            """
            :param lendo_dados_arq_cliente_txt(): Quando chama a função "consultar_cadastro_cliente", ela vai primeiro
            buscar as informações. Apos a informações serem adicionadas na lista "self.lista_dados_cliente", as
            informações serão destribuidas no dicionário "self.dados_cliente_dict"

            :return: depois das informações coletadas, os dados é impresso para o usuário.
            """
            for valor_consulta in self.lista_dados_cliente:
                print(f'{self.linhas_aparencia}\n')
                self.dados_cliente_dict = {'Nome:': valor_consulta[1],
                                           'CPF:': valor_consulta[0],
                                           'Idade:': valor_consulta[2],
                                           'E-mail:': valor_consulta[3]}
                for chave, valor in self.dados_cliente_dict.items():
                    print(f'{chave} {valor}')
            print(self.linhas_aparencia)
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
                print(f'\nNome: {valor_limpo_nome} CPF: {valor_limpo_cpf}\n'
                      f'você reservou {len(cadeiras_reservadas)} cadeiras')
                print('Cadeiras reservadas são:', end='')
                for valor in cadeiras_reservadas:
                    print(f'[{valor}]', end=' ')
                print(f'\nReserva feita na data: {data_reserva} - {hora_reserva}')
            print(self.linhas_aparencia)
            aperte_enter()

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

        def cadastrando_filmes():
            """
            :param: loop_listagem_arquivo: linha da função vai pega as informações dos filmes já cadastrados.
            :param: loop_principal_1: basicamente abrange toda função
            :param: loop_principal_2: esses parametros são responsavel por coletar as informações para a variavel
             registro_filmes e verificar se esta fora do padrão, e logo depois se possui duplicidade como descrito na
             proxima linha;
            :param: loop_registro: serve para coletar o número do registro e colocar variavel registro_filme, caso
            o registro não esteja com o parametro de 4 digitos, ele vai solicitar que digite novamente
            :param: loop_verificacao_duplicidade: depois que o loop_registro der tudo certo, ainda dentro do loop_registro,
             vai para o próximo paramentro, aqui ele vai buscar no objeto self.registros_filmes e ira verificar se
             o código que você digitou está já cadastrado, caso o codigo já esteja cadastrado, o loop quebra e
             volta para o loop_registro.
            :param: coleta_informacoes: apos todos os parametros estarem corretos, mas alinhas acima, o obejto
            self.quebra_loop ira receber que a condição é verdadeira e ira proceguir solicitando que adminitrador
            registre mais informações sobre o filme.
            :return: Apos tudo está finalizado, as informações serão salvas no arquivo "FILMES_CADASTRADOS.txt"
            """
            global abrindo_cadastro_filmes, registro_filme
            func_logo_cinema('AREA DE CADASTRO DE FILMES')
            lendo_dados_no_arq_filmes_txt()

            # loop_listagem_arquivo
            for registro_salvos in self.registros_filmes:
                print(f' Registro: [{registro_salvos[0]}] - [{registro_salvos[1]}]')
            print(self.linhas_aparencia)

            # loop_principal_1
            while True:
                try:
                    abrindo_cadastro_filmes = open(arq_cadastro_filmes_local_txt, 'a')
                except FileNotFoundError:
                    criando_arq_cadastro_filmes_txt = open(arq_cadastro_filmes_local_txt, 'w')
                    criando_arq_cadastro_filmes_txt.close()
                else:

                    # loop_principal_2
                    while True:

                        # loop_registro
                        while True:
                            registro_filme = str(input('Número de registro: '))
                            if len(registro_filme) != 4:
                                print('Registro fora padrão. '
                                      'O registro precisa possui 4 números!')
                                print(self.linhas_aparencia)
                                aperte_enter()
                            else:
                                print(self.linhas_aparencia)
                                break

                        # loop_verificacao_duplicidade
                        for registro_salvos_conf in self.registros_filmes:
                            if registro_filme == registro_salvos_conf[0]:
                                print(f'Codigo {registro_filme} já esta registrado [{registro_salvos_conf[1]}]')
                                print(self.linhas_aparencia)
                                aperte_enter()
                                self.quebra_loop = False
                                break
                            else:
                                self.quebra_loop = True  # Se o codigo não existir no registro, pode ser usado
                        if self.quebra_loop:
                            print(f'Código [{registro_filme}] sendo registrado!')
                            sleep(1)
                            break

                # coleta_informacoes
                if self.quebra_loop:
                    nome_filme_cadastro = input('Titulo: ')
                    genero_filme_cadastro = input('Genero: ')
                    duracao_filme_cadastro = input('Duração (min): ')
                    classificacao_filme_cadastro = leiaInt('Classificação(anos): ')
                    sinopse_filme_cadastro = str(input('Sinopse: ')).capitalize()
                    abrindo_cadastro_filmes.write(f'{registro_filme};'
                                                  f'{nome_filme_cadastro};'
                                                  f'{genero_filme_cadastro};'
                                                  f'{duracao_filme_cadastro};'
                                                  f'{classificacao_filme_cadastro};'
                                                  f'{sinopse_filme_cadastro} \n')
                    print('Filme cadastrado com sucesso')
                    sleep(1)
                    print(self.linhas_aparencia)
                    aperte_enter()
                    abrindo_cadastro_filmes.close()
                    resp_cadastro_filme = input('Cadastrar outro filme? [S/N]: ').upper()
                    if resp_cadastro_filme == 'N':
                        print('Voltando ao menu...')
                        sleep(1)
                        break
                else:
                    aperte_enter()
                    break

        # Corpo do programa
        def reservar_cadeira():
            """
            criar uma lista com os filmes em cartazes, com as informações disponivel, como sinopse, classificação
            inficativa; futuramento usar a internet para buscar essas informações.

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
                    print('Encontramos seu cadastro... !', end=' ')  # Avisa que encontro o cadastro
                    sleep(0.5)
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
                while True:
                    escolha_cliente = str(input('Escolha uma Poltrona (999 para Confirmar): ').upper())
                    if len(escolha_cliente) == 2:
                        break
                    elif escolha_cliente == '999':
                        break

                try:
                    valor_linha = escolha_cliente[0]
                    valor_coluna = int(escolha_cliente[1])
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
                    """
                    :param valores_reserva_1: recebe os valores da reserva em forme de lista. 
                    :param valores_reserva_cadeiras: recebe apenas as informações das cadeiras.
                    :param nome_cliente_reserva_cadeiras: recebe apenas os nome dos cliente.
                    :param loop confirmação das reservas: esse ação verifica quem foi o responsavel pela reserva. Casa
                    a verificação seja verdadeira, mostra o nome do cliente que reservou a cadeira. 
                    """

                    if cinema[valor_linha][valor_coluna] == '--':
                        for valores_reserva in self.lista_info_registro:
                            valores_reserva_1 = str(valores_reserva).split(';')
                            valores_reserva_cadeiras = valores_reserva_1[2:-2]
                            nome_cliente_reserva_cadeiras = valores_reserva_1[1]

                            # loop confirmação das reservas
                            for confir_cadeiras in valores_reserva_cadeiras:
                                if escolha_cliente == confir_cadeiras:
                                    print(self.linhas_aparencia)
                                    if nome_cliente == nome_cliente_reserva_cadeiras:
                                        print(f'Você reservou essa poltrona, sr. {nome_cliente}')
                                    else:
                                        print(
                                            f'Essa cadeira já foi reservada para o/a Sr(a).{nome_cliente_reserva_cadeiras}')
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

                if escolha_cliente == '999':
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
                                  f"Você reservou as seguintes "
                                  f"poltronas ==> {self.inf_reserva}")
                            gravando_reserva_cliente_txt(nome_reservado, cpf_reservado)
                            print(self.linhas_aparencia)
                            aperte_enter()
                            self.cadeiras_reservadas = cinema
                            atualizando_estrutura_cinema()
                            break

        def atualizando_estrutura_cinema():
            """
            :param: gravando_arq_reserva_restrutura. É responsavel por registrar as cadeiras que foram reservadas.
            Quando programa é fechado, as informações são retiradas da memória, então é precisa um registro em um
            arquivo de texto, que fica localizado no computador.
            :return:
            """
            gravando_arq_reserva_restrutura = open(arq_cadeiras_reservadas, 'w')
            for valor_reservas in self.cadeiras_reservadas:
                gravando_arq_reserva_restrutura.write(f'{valor_reservas}\n')
            gravando_arq_reserva_restrutura.close()

        def area_admin():
            func_data_atual()
            while True:

                func_logo_cinema('Area do Administração')
                print(
                    f"""
                      Hora certa
        |                                     |
        |         {self.data_atual} - {self.hora_atual}       |
        |_____________________________________|
        {self.linhas_aparencia}      
        | [1] | Consultar cadastro cliente
        | [2] | Cadastrar Filmes no sistema
        | [3] | Colocar filme em cartaz
        | [4] | Consultar todas as reservas no sistema       
        | [5] | Filmes em cartaz
        | [6] | Consultar cadeiras disponiveis
        | [0] | Voltar ao menu principal
        {self.linhas_aparencia}""")
                resp_admin = leiaInt('Escolha uma opção: ')

                # Consultando cadastro dos clientes.
                if resp_admin == 1:
                    if len(self.lista_dados_cliente) == 0:
                        print(self.linhas_aparencia)
                        print('• Não existe nenhum cliente cadastrado')
                        print('• Volta ao menu principal e escolha a opção "2" para realizar um cadastro.')
                        print(self.linhas_aparencia)
                        aperte_enter()
                    else:
                        consultar_cadastro_cliente()

                # Cadastrando um filme no sistema.
                elif resp_admin == 2:
                    cadastrando_filmes()

                # Colocar um filme em cartaz.
                elif resp_admin == 3:
                    gravando_filmes_em_cartaz()

                # Consultar todas as reservas no sistema
                elif resp_admin == 4:
                    consultar_registro_reserva()
                    if len(self.lista_info_registro) == 0:
                        print(self.linhas_aparencia)
                        print('Não encontrei nenhum registro no sistema. '
                              'Verifique se a sessão já terminou...')

                elif resp_admin == 5:
                    func_listando_filmes_cartaz()

                elif resp_admin == 6:
                    print('<desenvolvimento>')

                elif resp_admin == 0:
                    print('<desenvolvimento>')
                    break

        def area_cliente():
            func_data_atual()
            while True:
                print(
                    f"""
                          Hora certa
            |                                     |
            |         {self.data_atual} - {self.hora_atual}       |
            |_____________________________________|
            {self.linhas_aparencia}            
            | [1] | Escolha um filme
            | [2] | Cadastrar USUÁRIO
            | [3] | Consultar sua reserva
            | [0] | Sair 
            {self.linhas_aparencia}""")
                resp_cliente = leiaInt('Escolha uma opção: ')

                if resp_cliente == 1:
                    reservar_cadeira()

                elif resp_cliente == 2:
                    cadastro_cliente()

                elif resp_cliente == 3:
                    lendo_dados_no_arq_reserva()
                    self.lista_info_registro
                    while True:
                        print(self.linhas_aparencia)
                        lendo_cpf_cliente = leiaInt('Digite seu cpf: ')
                        for valor_cpf in self.lista_info_registro:
                            valor_format = str(valor_cpf).split(';')
                            cpf_cliente_txt = valor_format[0].strip()
                            nome_cliente_txt = valor_format[1].strip().title()
                            cpf_cliente_int = int(cpf_cliente_txt)
                            cadeiras_cliente = valor_format[2:-2]
                            if cpf_cliente_int == lendo_cpf_cliente:
                                print(f'Bem vindo Sr(a) {nome_cliente_txt} \n'
                                      f'Você reservou as seguintes poltronas: ', end=' ')
                                for valor_cadeiras in cadeiras_cliente:
                                    print(f'[{valor_cadeiras}]', end=' ')
                            else:
                                print(f'Com o CPF {lendo_cpf_cliente}, não encontramos nenhuma reserva.')
                        print(f'\n{self.linhas_aparencia}')
                        resp_consulta = str(input('\nRealizado outra consulta? [S/N]: ')).upper()
                        if resp_consulta == 'N':
                            print('Voltando para o menu...!')
                            sleep(1)
                            break

                elif resp_cliente == 0:
                    print(self.linhas_aparencia)
                    print('Voltando ao menu principal...')
                    sleep(1)
                    break
                else:
                    print('Voce entrou com uma opção errada!')

        """
        Sobre as variaveis abaixo do texto.
        :param cinema: Pega as informações na função "sala_cinema" para criar a estrutura que o usuário ira visualizar.
        :param lendo_dados_arq_cliente_txt: quando o programa abrir, ele vai pegar as informações do cliente no banco de 
        dados e deixá-lo disponivel para o sistema utilizar conforme necessidade. 
        :param lendo_dados_no_arq_reserva: depois que as informações do cliente estiverem disponivel, sera preciso colocar
        as informações de reservas, como, nome e cpf do cliente que reservou, quais as cadeiras reservadas, etc. Essas 
        informações serão necessarias para saber quem reservou as cadeiras.
        """
        cinema = sala_cinema()
        lendo_dados_arq_cliente_txt()
        lendo_dados_no_arq_reserva()

        # Menu principal
        while True:
            func_data_atual()
            print(
                f'''
                      Hora certa
        |                                     |
        |              {self.hora_atual}               |
        |_____________________________________|
        {self.linhas_aparencia}
        | [1] |  Area do CLIENTE      
        | [2] |  Area da administração
        | [0] |  Sair
        {self.linhas_aparencia} ''')
            resp_menu_principal = leiaInt('        Escolha uma opção: ')

            # Menu clientes
            if resp_menu_principal == 1:
                area_cliente()

            # Menu administração
            elif resp_menu_principal == 2:
                area_admin()

            # OPÇÃO SAIR
            elif resp_menu_principal == 0:
                print(self.linhas_aparencia)
                print('Fechando o programa')
                sleep(1)
                break
            else:
                print('Opção invalida!')


abrindo_cinema = SalaCinema()
