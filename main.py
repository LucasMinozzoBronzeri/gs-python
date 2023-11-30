#Diego Costa Silva RM552648
#Lucas Minozzo Bronzeri RM553745
#Marcelo Mendes Galli RM553654

contcadastro = 1
contnome = 1
contdata = 1
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

#variaveis para salvar as informações de cadastro
nome = 0
senha = 0
data = 0


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
