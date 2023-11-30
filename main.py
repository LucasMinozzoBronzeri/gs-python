#Diego Costa Silva RM552648
#Lucas Minozzo Bronzeri RM553745
#Marcelo Mendes Galli RM553654

contcadastro = 1
contlogin = 1
contmenu = 1
contnome = 1
contdata = 1
contcpf = 1
contsenha = 1

#validação da data
def data_valida(data):
    try:
        # faz o split e transforma em números
        dia, mes, ano = map(int, data.split('/'))

        # mes ou ano inválido, retorna False
        if mes < 1 or mes > 12 or ano <= 0:
            return False

        # verifica qual o último dia do mês
        if mes in (1, 3, 5, 7, 8, 10, 12):
            ultimo_dia = 31
        elif mes == 2:
            if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                ultimo_dia = 29
            else:
                ultimo_dia = 28
        else:
            ultimo_dia = 30

        # verifica se o dia é válido
        if dia < 1 or dia > ultimo_dia:
            print('Data invalida!!!')
            return False


        return True
    except ValueError:
        return False

#validação cpf
def cpf_valido(cpf):
            if len(cpf) == 11:
                primeiro1 = int(cpf[0]) * 10
                primeiro2 = int(cpf[1]) * 9
                primeiro3 = int(cpf[2]) * 8
                primeiro4 = int(cpf[3]) * 7
                primeiro5 = int(cpf[4]) * 6
                primeiro6 = int(cpf[5]) * 5
                primeiro7 = int(cpf[6]) * 4
                primeiro8 = int(cpf[7]) * 3
                primeiro9 = int(cpf[8]) * 2

                seg_primeiro1 = int(cpf[0]) * 11
                seg_primeiro2 = int(cpf[1]) * 10
                seg_primeiro3 = int(cpf[2]) * 9
                seg_primeiro4 = int(cpf[3]) * 8
                seg_primeiro5 = int(cpf[4]) * 7
                seg_primeiro6 = int(cpf[5]) * 6
                seg_primeiro7 = int(cpf[6]) * 5
                seg_primeiro8 = int(cpf[7]) * 4
                seg_primeiro9 = int(cpf[8]) * 3
                seg_primeiro10 = int(cpf[9]) * 2

                contaprimeiro = 11-((primeiro9 + primeiro8 + primeiro7 + primeiro6 + primeiro5 + primeiro4 + primeiro3 + primeiro2 + primeiro1)%11)

                contaseg = 11 -((seg_primeiro10 + seg_primeiro9 + seg_primeiro8 + seg_primeiro7 + seg_primeiro6 + seg_primeiro5 + seg_primeiro4 + seg_primeiro3 + seg_primeiro2 + seg_primeiro1)%11)

                doisultnum = (int(cpf[9]) * 10)+ int(cpf[10])

                somaprimeiroeseg = (contaprimeiro * 10) + contaseg

                if doisultnum == somaprimeiroeseg:
                    return True

                elif doisultnum != somaprimeiroeseg:
                    return False

#variaveis para salvar as informações de cadastro
nome = 0
senha = 0
data = 0
cpf = 0


while contcadastro != 0:
    print('=== Cadastrar ===')

    #Nome

    while contnome != 0:

        nome = str(input('Nome Completo: '))

        #validação do nome

        if len(nome) <= 2:
            print('O Nome deverá ter no mínimo 3 letras!!!')
            contnome += 1

        else:
            if contnome:
                break


    #data de nascimento

    while contdata != 0:
        data = data_valida(str(input('Data de nascimento: ')))
        if data == False:
            contdata += 1

        elif data == True:
            if contdata:
                break


    #CPF


    while contcpf != 0:

        cpf = cpf_valido(str(input('CPF: ')))

        if cpf == True:
            if contcpf:
                break

            elif contcpf == False:
                contcpf += 1

    #Senha

    while contsenha != 0:
        print('* A senha deve conter pelo menos 7 digitos')
        print('* Pelo menos uma letra maiúscula')
        print('* Pelo menos 1 número')
        print('* Pelo menos um caractere especial')
        senha = str(input('Senha: '))


        #validação senha

        while len(senha) <= 6:
            senha = input('* A senha deve conter pelo menos 7 numeros ou letras: ')

        while senha.islower():
            senha = input('* A senha deve conter pelo menos uma caractere maiúsculo: ')

        while senha.isalpha():
            senha = input('* A senha deve conter pelo menos 1 numeros: ')

        while senha.isalnum():
            senha = input('* A senha deve conter pelo menos um caractere especial: ')

        if contcadastro:
            break

    while contlogin != 0:

        print('=== Fazer Login ===')

        nome1 = str(input('Nome: '))

        senha1 = str(input('Senha: '))

        if nome1 != nome or senha1 != senha:
            print('Nome ou senha inválidos!!!')
            contlogin += 1

        if nome1 == nome and senha1 == senha:
            if contlogin:
                break

    while contmenu != 0:

        print('=== Menu Inicial ===')
        print('1 - Marcar consulta')
        print('2 - Guia para Gestantes')
        print('3 - Quem somos?')
        print('0 - Sair')
        opcao = int(input())

        if opcao == 1:
            print('Aqui o usuario poderia marcar uma data pra ter uma consulta mais aprofundada '
                  'e desenvolver melhor as informações sobre sua saúde.')

            contmenu += 1

        elif opcao == 2:
            print('Exames:')
            print('     -Exames de sangue;')
            print('     -Exame de urina;')
            print('     -Exame de fezes;')
            print('     -Exame ginecológicos;')
            print('     -Ultrassom;')
            print('     -Triagem de estreptococo;')
            print('\n\nBoa Alimentação:')
            print('     -Frutas frescas(maçãs, bananas, morangos, uvas etc.)')
            print('     -Vegetais variados(brócolis, espinafre, cenouras,abobrinha etc.)')
            print('     -Grãos integrais(arroz integral, quinoa, aveia etc.)')
            print('     -Legumes(feijão, lentilhas, grão-de-bico etc)')
            print('     -Proteínas magras(frango, peixe, tofu, carne magra, ovos)')
            print('\n\nBoa Alimentação para o Bebê:')
            print('     De 6 a 7 meses:')
            print('             -Purê de abacate;')
            print('             -Purê de banana;')
            print('             -Purê de batata doce;')
            print('             -Purê de cenoura.')
            print('     De 8 a 9 meses:')
            print('             -Feijão e arros(muito bem cozidos)')
            print('             -Purê de batata;')
            print('             -Purê de banana;')
            print('             -Purê de batata doce;')
            print('             -Purê de cenoura.')
            print('     De 10 a 12 meses:')
            print('             -Feijão e Arroz;')
            print('             -Pequenos pedaços de carne e frango;')
            print('             -Pedaços de manga;')
            print('             -Uva sem caroço;')
            print('             -Mamão.')

            contmenu += 1


        elif opcao == 3:
            print('Nosso é oferecer assistência médica e odontológica de alta qualidade a preços '
                      'acessíveis.')
            print('\nNossos processos são regularmente revisados pelo Conselho de Administração de forma '
                      'consolidada para embasar as decisões estratégicas.')
            print('\nA estrutura organizacional da empresa inclui hospitais, pronto-atendimentos, clínicas '
                      'e outras unidades de atendimento, todos destinados a atender às necessidades dos beneficiários dos produtos'
                      'comercializados pela operadora de planos de saúde.')
            print('\nA empresa opera através de dois tipos de produtos: Plano de Assistência Médica e '
                      'Planos de Assistência Odontológica, distribuídos geograficamente.')

            contmenu += 1

        elif opcao == 0:
            exit()
