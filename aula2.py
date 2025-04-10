#Lista de Exercícios Estrutura de Decisão
import datetime
#TODO 01
# number = float(input("Coloque um número: "))
# if number > 0:
#     print(f"O Número {number} é positivo")
# elif number == 0:
#     print(f"Esse é o zero")
# else: print(f"O Número {number} é negativo")

#TODO 02
# var = float(input("Coloque um número: "))
# if var > 10:
#     print(f"{var} é maior que 10")
# else: print(f"{var} é menor que 10")

#TODO 03
# a = float(input("Coloque número: "))
# b = float(input("Coloque outro número: "))
# if a + b > 10:
#     print(f"{a+b} é MAIOR que 10")
# elif a + b == 10:
#     print(f"{a+b} é 10" )
# else: print(f"{a+b} é MENOR que 10")

#TODO 04
# numero = float(input("Coloque um número: "))
# if numero % 5 == 0:
#     print(f"{numero} é divisível por 5")
# else: print(f"{numero} não é divisível por 5")

#TODO 05
# numero = float(input("Coloque um número: "))
# if numero > 20 and numero < 90:
#     print(f"{numero} Está entre 20 e 90")
# else: print(f"{numero} NÃO está entre 20 e 90")

#TODO 06
dataAtual = datetime.date.today()
# anoNasc = int(input("Ano que nasceu (2000): "))
# if dataAtual.year - anoNasc >= 16:
#     print (f"Você ja pode votar")
# else: print("Você ainda não pode votar")

#TODO 07
# anoNasc = int(input("Ano que nasceu (2000): "))
# idade = dataAtual.year - anoNasc
# if anoNasc <= 0 or anoNasc > dataAtual.year:
#     print ("Impossivel esse ano não existe, não nesse sistema")
# else: print(f"Você tem ou teria {idade} anos")

#TODO 08
# idade = int(input("Sua idade: "))
# if idade >= 18 and idade <= 65:
#     print("Você é de Maior")
# elif idade < 0:
#     print("Você não nasceu ainda")
# elif idade < 18:
#     print("Você é DMenor")
# else: print("Acima de 65 anos")

#TODO 09
# nota1 = float(input("Coloque a nota da Prova 1: "))
# nota2 = float(input("Coloque a nota da Prova 2: "))
# nota3 = float(input("Coloque a nota da Prova 3: "))

# media = (nota1 + nota2 + nota3) / 3
# if media >= 6:
#     print(f"\033[32m {f'Você foi aprovado(a), sua média foi {media}'}")
# else: print(f"\033[31m{f'Você foi reprovado(a), sua média foi {media}'}")

#TODO 10
# nota4 = float(input("Coloque a nota da Prova 4: "))
# nota5 = float(input("Coloque a nota da Prova 5: "))

# media2 = (nota4 + nota5) / 2

# if media2 < 7:
#     print(f"\033[33m EXAME")
#     notaExame = float(input("Coloque a nota do Exame: "))
#     if notaExame < 5:
#         print(f"\033[31m REPROVADO")
#     else: print(f"\033[32m APROVADO")
# else: print(f"\033[32m APROVADO")

#TODO 11
# nome = input("Escreva seu Nome: ")
# qtdHoras = float(input("Qunatia de horas de aula: "))
# qtdPorHora = float(input("Ganhos por horas de aula: "))

# ganhos = qtdHoras * qtdPorHora

# nome2 = input("Escreva seu Nome: ")
# qtdHoras2 = float(input("Qunatia de horas de aula: "))
# qtdPorHora2 = float(input("Ganhos por horas de aula: "))

# ganhos2 = qtdHoras2 * qtdPorHora2

# if ganhos < ganhos2:
#     print(f"O Professor {nome2} ganha mais")
# else: print(f"O Professor {nome} ganha mais")

#TODO 12
# parImpar = int(input("Coloque um numero: "))
# if parImpar % 2 == 0:
#     print("É par")
# else: print("É impar")

#TODO 13
# timeA = input("Nome do Time: ")
# golsA = int(input("Quantia de gols do time: "))

# timeB = input("Nome do Time: ")
# golsB = int(input("Quantia de gols do time: "))

# if golsA < golsB:
#     print(f"O Time do {timeB} foi Vencedor")
# elif golsB == golsA:
#     print("EMPATE")
# else: print(f"O Time do {timeA} foi Vencedor")

#TODO 14
# cidade = ['Carioca', 'Paulista', 'Mineiros', 'Outros']
# siglas = ['RJ', 'SP', 'MG']
# sigla = input("Sigla do seu estado: ")
# if sigla == 'RJ':
#     print(cidade[0])
# elif sigla == 'SP':
#     print(cidade[1])
# elif sigla == 'MG':
#     print(cidade[2])
# else: print(cidade[3])

#TODO 15
# produto = float(input("Valor do produto: "))
# if produto < 20.00:
#     print (f"R$ {((produto * 45 / 100) + produto):.2f}")
# else: print(f"R$ {((produto * 30 / 100) + produto):.2f}")

#TODO 16
mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Novembro', 'Dezembro']
numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
number = int(input("Escolha um numero: "))

for i in numb:
    nmes = (numb[i], mes[i])

    print(nmes)