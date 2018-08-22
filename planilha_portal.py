#*************************************************************#
#Software totalmente feito e revisado por Leonardo henrique#
#Autor: Leonardo Henrique Martins Ferreira#
#Ciências da computação e profissão#
#Campos Pitágoras Turo#
#Linguagem de programação usada Python#
#Codigo aberto porém somente com creditos a Leonardo Henrique#
#*************************************************************#

'''#Informações do usuario obtidas para o banco de dados#'''
import os

#Inicio do programa

print("\t||Bem vindo ao nosso software automatizade de cadastro das notas dos alunos||")
print("\t||Software com codigo aberto, porém somente com creditos a Leonardo Henrique||")
print("\t\t\t\t(Versão 1.0.1 beta)")

input ("\nPara iniciar o cadastro do seu banco de dados tecle enter.\n")

print("-----------------")
print("Vamos começar.")
print("-----------------")

#Coletando informações do mesmo
print("\nObservação: De um nome para o arquivo de suas informações pessoais.")
print("Observação2: Aconcelhamos o seu nome para ficar mais facil a indentificação.")

#Nome dos arquivos craidos
nomeinfo = input("\n|Nome para a data base de suas informações: ")
nomedados = input("\n|Nome para a data base das notas dos alunos: ")
print("\n||Criando diretório de dados, todos os arquivos serão salvos em 'C:/PAD Notes'||\n")

#Criando pastas

try:
    os.makedirs('C:/PAD Notes/Informacoes')
    os.mkdir('C:/PAD Notes/Logins')
    os.mkdir('C:/PAD Notes/Notas')
    input("Diretórios criados, tecle enter para continuar...\n")
except FileExistsError:
    print("------------------------------------------------------------------------------------------------------------------")
    print("|Error: Diretório de arquivos ja existentes, não necessarios criar novos diretórios, acesse a pasta 'C:/PAD Notes'")
    print("------------------------------------------------------------------------------------------------------------------")
input("\nTecle enter para continuar com o cadastro.")
        
#Informaçoes    
informacoes = []
nomeprof = input("\n|Nome do professor: ")
nomefacul = input("\n|Nome da Instituição: ")
curso = input("\n|Nome do curso: ")

#Testes de bugs
while True:
    try:
        periodo = int(input("\n|Periodo letivo: "))
        break
    except ValueError:
        print("\t\nError: ||Somente estes formatos são permitidos (1, 2, 8, 6)||")


while True:
    try:
        data = int(input("\n|Data ano letivo(ex:2015): "))
        break
    except ValueError:
        print("\t\nError: ||Somente estes formatos são permitidos (2010, 2015)||")

disciplina = input("\n|Disciplina: ")

while True:
    try:
        diasletivos = int(input("\n|Dias letivos: "))
        break
    except ValueError:
        print("\t\nError: ||Somente estes formatos são permitidos (10, 1, 3)||")

while True:
    try:
        sala = int(input("\n|Numero da sala: "))
        break
    except ValueError:
        print("\t\nError: ||Somente estes formatos são permitidos (310, 303)||")

coordenador = input("\n|Digite o nome do coordenador: ")

while True:
    try:
        totalalunos = int(input("\n|Quantos alunos vão ser cadastrados?: "))
        break
    except ValueError:
        print("\t\nError: ||Somente estes formatos são permitidos (3, 19, 50)||")

#Salvando informaçoes e teste de usuario
usuario = input("\n|Nome de usuario: ")
senha = input("\n|Senha: ")

informacoes.append("\n")
informacoes.append("-------------------------------------------------------")
informacoes.append("\nNome do Professor: \t%s" %(nomeprof))
informacoes.append("\nNome da Instituição: \t%s" %(nomefacul))
informacoes.append("\nNome do curso: \t%s" %(curso))
informacoes.append("\nPeriodo letivo: \t%s" %(periodo))
informacoes.append("\nData ano letivo: \t%s" %(data))
informacoes.append("\nDisciplina: \t%s" %(disciplina))
informacoes.append("\nDias letivos: \t%s" %(diasletivos))
informacoes.append("\nNumero da sala: \t%s" %(sala))
informacoes.append("\nDigite o nome do coordenador: \t%s" %(coordenador))
informacoes.append("\nDigite a nota de corte: \t7")
informacoes.append("\nQuantos alunos vão ser cadastrados?: \t%s" %(totalalunos))
informacoes.append("\nUsuario: \t%s" %(usuario))
informacoes.append("\nSenha: \t%s" %(senha))
informacoes.append("\n-----------------------------------------------------")
informacoes.append("\n")

#salvando informações em arquivo
informacoestxt = open("C:/PAD Notes/Informacoes/%s.csv" %(nomeinfo), 'a+')
informacoestxt.writelines(informacoes)
informacoestxt.close()
print("\n--------------------------------------------------------")
print("Todos os dados foram salvos em nosso banco de dados... ")
print("--------------------------------------------------------")
print("\n\nPara cadastrar os aluno por favor entre com seu usuario e senha.")

'''Usuario ja cadastrado'''

#Teste de login de usuario não cadastrado

loginteste = open("C:/PAD Notes/Logins/login.txt", 'a+')
loginteste.write(usuario)
loginteste.close()

senhateste = open("C:/PAD Notes/Logins/senhas.txt", 'a+')
senhateste.write(senha)
senhateste.close()

print("|---------------------|")
login = input("|Usuario: ")
logins = input("|Senha: ")
print("|---------------------|")

loginarq = open("C:/PAD Notes/Logins/login.txt", 'r')
loginarq2 = loginarq.read()
loginarq.close()

senhaarq = open("C:/PAD Notes/Logins/senhas.txt", 'r')
senhaarq2 = senhaarq.read()
senhaarq.close()

#Caso erre a senha
if login == usuario in loginarq2 and logins == senha in senhaarq2:
    print("\n|Logado, acessando a area de cadastro dos alunos...|")
else:
    while login != usuario in loginarq2 and logins != senha in senhaarq2:
        print("\n|Error: Usuario ou senha incorreta tente novamente:")
        print("-----------------------------------------------------")
        print("|---------------------|")
        login = input("Usuario: ")
        logins = input("Senha: ")
        print("|---------------------|")

print("\n|Logado, acessando a area de cadastro dos alunos...|")
'''#Cadastrar alunos#'''
print("---------------------------------------------------------------------------------------------------")
print("Observação: Se o aluno não fez a oficial 1 ou 2 colocar 0 na nota.")
print("Observação 2: coloque os nomes em ordem alfabetica, não quero ter trabalho de organizar para você!!")
print("---------------------------------------------------------------------------------------------------")
input("Digite enter para continuar")

'''#Funções matematicas do programa#'''

#laço de alunos
cont = 1
while cont <= totalalunos:
    aluno = str(input("\n|Digite o nome do aluno: "))

#Testes de numeros
    while True:
        try:
            notap1 = float(input("\n|Digite a nota da parcial 1: "))
            break
        except ValueError:
            print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
    notap1c = notap1 * 0.3

    while True:
        try:
            notaof1 = float(input("\n|Digite a nota da oficial 1: "))
            break
        except ValueError:
            print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
    notaof1c = notaof1 * 0.7

#Notas do bloco 1
    notabloco1 = notap1c + notaof1c
    notabloco1c = notap1c + notaof1c
    notabloco1c2 = notabloco1c * 0.4

#Testes de numeros
    while True:
        try:
            notap2 = float(input("\n|Digite a nota da parcial 2: "))
            break
        except ValueError:
            print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
    notap2c = notap2 * 0.3

#Testes de numeros
    while True:
        try:
            notaof2 = float(input("\n|Digite a nota da oficial 2: "))
            break
        except ValueError:
            print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
    notaof2c = notaof2 * 0.7

#Nota bloco 2
    notabloco2 = notap2c + notaof2c
    notabloco2c = notap2c + notaof2c
    notabloco2c2 = notabloco2c * 0.6

#Segunda chamada
    if notaof1 == 0:
        while True:
            try:
                print("\nNão detectado nota da primeira oficial do aluno, por favor.")
                print("---------------------------------------------------")
                notaof1sc = float(input("|Digite a nota da 2 chamada oficial 1: "))
                print("---------------------------------------------------")
                if notaof1sc > 0:
                    notaof1 = notaof1sc
                    notaof1c = notaof1sc * 0.7
                    notabloco1 = notap1c + notaof1c
                    notabloco1c = notap1c + notaof1c
                    notabloco1c2 = notabloco1c  * 0.4
                break
            except ValueError:
                print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
        notaof1scc = notaof1sc * 0.7
    elif notaof1 > 0:
        notaof1sc = 0

    if notaof2 == 0:
        while True:
            try:
                print("\nO aluno não tem nota da segunda oficial por favor.")
                print("---------------------------------------------------")
                notaof2sc = float(input("|Digite a nota da 2 chamada oficial 2: "))
                print("---------------------------------------------------")
                if notaof2sc >=0:
                    notaof2 = notaof2sc
                    notaof2c = notaof2sc * 0.7
                    notabloco2 = notap2c + notaof2c
                    notabloco2c = notap2c + notaof2c
                    notabloco2c2 = notabloco2c  * 0.6
                break
            except ValueError:
                print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
        notaof2scc = notaof2sc * 0.7
    elif notaof2 > 0:
        notaof2sc = 0
    print("\n\t**Aluno cadastrado**\n")
    cont += 1

#Notas da segunda chamada
    notaof1ccs = notaof1sc
    notaof2ccs = notaof2sc

#Medias simestral
    medias = notabloco1c2 + notabloco2c2

    '''#Documentação para ser salva no banco de dados#'''

    documentacao = []
    documentacao.append("\n--------------------------------------------------------------------------")
    documentacao.append("\nAluno: %s" %(aluno))
    documentacao.append("\n--------------------------------------------------------------------------")
    documentacao.append("\nNotas")
    documentacao.append("\n                     ||Bloco 1||")
    documentacao.append("\nNota da prova parcial 1: \t%.2f" %(notap1))
    documentacao.append("\nNota da prova parcial 1 convertida (30 porcento): \t%.2f" %(notap1c))
    documentacao.append("\n")
    documentacao.append("\nNota da prova oficial 1: \t%.2f" %(notaof1))
    documentacao.append("\nNota da prova oficial 1 convertida (70 porcento): \t%.2f" %(notaof1c))
    documentacao.append("\n")
    documentacao.append("\nNota Bloco 1: \t%.2f" %(notabloco1))
    documentacao.append("\nNota bloco 1: (40 porcento) \t%.2f" %(notabloco1c2))
    documentacao.append("\n--------------------------------------------------------------------------")
    documentacao.append("\n                     ||Bloco 2||")
    documentacao.append("\nNota da prova parcial 2: \t%.2f" %(notap2))
    documentacao.append("\nNota da prova parcial 2 convertida (30 porcento): \t%.2f" %(notap2c))
    documentacao.append("\n")
    documentacao.append("\nNota da prova oficial 2: \t%.2f" %(notaof2))
    documentacao.append("\nNota da prova oficial 2 convertida (70 porcento): \t%.2f" %(notaof2c))
    documentacao.append("\nNota Bloco 2: \t%.2f " %(notabloco2))
    documentacao.append("\nNota bloco 2: (60 porcento) \t%.2f" %(notabloco2c2))
    documentacao.append("\n--------------------------------------------------------------------------")
    documentacao.append("\nNota da segunda chamada oficial 1: \t%.2f" %(notaof1ccs))
    documentacao.append("\nNota da segunda chamada oficial 2: \t%.2f" %(notaof2ccs))
    documentacao.append("\nMedia simestral \t%.2f" %(medias))

#Testando as medias antes de salvar
    if medias >= 7:
        print("|==Medias calculadas e o aluno foi aprovado com nota em media.==|")
        documentacao.append("\n\nSituação final: \t||Aprovado por media||")
    if medias < 7:
        while True:
            try:
                print("\n|==Medias calculadas e aluno ficou de final.==|\n")
                examef = float(input("\|nDigite o valor do exame final: "))
                break
            except ValueError:
                print("\t\nError: ||Somente numeros são permitidos (1, 10, 1.0)||")
        final1 = (medias + examef) / 2
        if final1 >= 7:
            documentacao.append("\n\nExame final: \t%.2f" %(examef) )
            documentacao.append("\nMedia final: \t%.2f" %(final1))
            documentacao.append("\n\nSituação final: \t||Aprovado por Final||")
        else:
            documentacao.append("\n\nExame final: \t%.2f" %(examef) )
            documentacao.append("\nMedia final: \t%.2f" %(final1))
            documentacao.append("\n\nSituação final: \t||Reprovado por Final||")
    documentacao.append("\n--------------------------------------------------------------------------")

#Salvando banco de dados de notas
    alunostxt = open("C:/PAD Notes/Notas/%s.csv" %(nomedados), 'a+')
    alunostxt.writelines(documentacao)
    alunostxt.close()

#fim do programa
print("\n||Todos os dados foram salvos com sucesso...||")
print("\n||Para conferir os seus dados completos e as notas dos alunos cadastrados acesse a pasta do nosso software 'C:/PAD Notes/Notas' e procure as Databases com o seu nome ou o que voce escolheu.||")
input("||Tecle enter para sair...||")
