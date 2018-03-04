'''Tela de boas vindas'''

print('\nWell, here we started your register in our program, please follow at instructions below!!!')

'''Iniciando o programa'''

raw_input("\n\tPress enter to continue...\t")

'''variaveis do programa'''

fn = raw_input('\nFull name: ')

un = raw_input('\nUser name: ' )

from datetime import datetime
def date(entrada):
    try:
        datetime.strptime(entrada, '%m/%d/%Y')
        return True
    except ValueError:
        return False
while date(raw_input('\nDate of birth: ')) == False:
    print('!==Wrong date, please use "MM/DD/YY"==!')

while True:
    try:
        cpf = int(raw_input("\nCPF: "))
        break
    except ValueError:
        print("\t\n!==Type only number==!")

pw = raw_input("\nPassword: ")

print ('\nSaving Information, Please wait...')

print('Great... Register successful ')

cont = raw_input("\nPress enter to log in...")
'''Salvando em arquivo'''

arquivo = open('dados.txt', 'w')
arquivo.write("Full name: %s\n" %(fn))
arquivo.write("User name: %s\n" %(un))
arquivo.write("Password: %s\n" %(pw))
arquivo.close()

'''Tentando Logar'''

print("\n\tSing in")

user_name = raw_input("\nUser name: ")

password = raw_input("Password: ")

'''Caso erre o UN e o PW'''

while 1:
    if user_name == un and password == pw:
        print('\nCongratulations, Logged')
        break
    else:
        print("\nName or password incorrect, try again...")

        user_name = raw_input("\nUser name: ")
        password = raw_input("Password: ")
