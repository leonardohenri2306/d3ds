'''Tela de boas vindas'''

teste = int(input("\nWelcome to our program if you are already registered please press '1', if not press '2', for read base files press '3'."))
if teste == 1:

    print('\nWell, here we started your register in our program, please follow at instructions below!!!')
    '''Iniciando o programa'''

    input("\n\tPress enter to continue...\t")

    '''variaveis do programa'''

    fn = input('\nFull name: ')

    un = input('\nUser name: ' )

    from datetime import datetime
    def date(entrada):
        try:
            datetime.strptime(entrada, '%m/%d/%Y')
            return True
        except ValueError:
            return False
    while date(input('\nDate of birth: ')) == False:
        print('!==Wrong date, please use "MM/DD/YY"==!')

    while True:
        try:
            cpf = int(input("\nCPF: "))
            break
        except ValueError:
            print("\t\n!==Type only number==!")

    pw = input("\nPassword: ")

    print ('\nSaving Informations, Please wait...')

    print('Great... Register successful ')

    '''Salvando em arquivo'''

    arquivo = open('dados.txt', 'a+')
    files = []
    files.append("\nUsuario %s\n" %(fn))
    files.append("Full name: %s\n" %(fn))
    files.append("User name: %s\n" %(un))
    files.append("Password: %s\n" %(pw))
    arquivo.writelines(files)
    arquivo.close()

    '''Lendo as informações'''
    print("=================================================================")
    print("To read your recorded informations reopen the program and type 3.")
    print("=================================================================")

if teste == 2:
    print("\n\tOk, lets check out")
    cont = input("\nPress enter to log in...")

    print("\n\tSing in")

    user_name = input("\nUser name: ")

    password = input("Password: ")

    '''Caso erre o UN e o PW'''

    if user_name == un and password == pw:

        print('\nCongratulations, Logged')

    else:
        print("\nName or password incorrect, try again...")
        user_name = input("\nUser name: ")
        password = input("Password: ")

if teste == 3:
    print("\t\nType the name and password for informations\n")
    name = str(input("Type name: "))
    pass2 = input("Type password: ")

    arquivo3 = open('dados.txt', 'r')
    text2 = arquivo3.read()

    if name in text2:
        pass1 = input("\nUser found, please type your password for confirmation. ")
        if pass1 == pass2:
            print("\t\tBase Files")
            print("=================================================")
            print(text2)
            print("=================================================")
        else:
            print("Password incorrect please try again later...")
    else:
        print("Sorry, name not found..\n")
    arquivo3.close()
