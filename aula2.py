#Lista de Exercícios Estrutura de Decisão
import datetime, math
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

#TODO 13bhaskara
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
# mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro','Novembro', 'Dezembro']
# number = int(input("Escolha um numero: "))
# elif number == 1:
#     print(mes[0])
# elif number == 2:
#     print(mes[1])
# elif number == 3:
#     print(mes[2])
# elif number == 4:
#     print(mes[3])
# elif number == 5:
#     print(mes[4])
# elif number == 6:
#     print(mes[5])
# elif number == 7:
#     print(mes[6])
# elif number == 8:
#     print(mes[7])
# elif number == 9:
#     print(mes[8])
# elif number == 10:
#     print(mes[9])
# elif number == 11:
#     print[mes[10]]
# elif number == 12:
#     print(mes[11])
# else: print(f"\033[31m ERROR")

#TODO 17
# vogal = ['A', 'E', 'I', 'O', 'U', 'Y']
# letra = input("Coloque uma letra: ").upper()
# if letra == vogal[0]:
#     print("Vogal")
# elif letra == vogal[1]:
#     print("Vogal")
# elif letra == vogal[2]:
#     print("Vogal")
# elif letra == vogal[3]:
#     print("Vogal")
# elif letra == vogal[4]:
#     print("Vogal")
# elif letra == vogal[5]:
#     print("Vogal")
# else:print("Consoante")

#TODO 18
# a = int(input("Coloque um numero: "))
# b = int(input("Coloque outro numero: "))

# if a < b:
#     print(b)
# else: print (a)

#TODO 19
# a = int(input("Coloque um numero: "))
# b = int(input("Coloque outro numero: "))

# if a < b:
#     print(a , b)
# else: print (b , a)

#TODO 20
# a = int(input("Coloque um numero: "))
# b = int(input("Coloque outro numero: "))
# c = int(input("Coloque outro numero: "))

# if a != b and b != c and c != a:
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#      print (b)
#     else: print(c)
# else: print("Numeros Iguais")

#TODO 21
# a = int(input("Coloque um numero: "))
# b = int(input("Coloque outro numero: "))
# c = int(input("Coloque outro numero: "))
# if a != b and b != c and c != a:
#     if a > b and b > c:
#         print(a + b)
#     elif c > a and a > b:
#         print (c + a)
#     else: print(c + b)
# else: print("Numeros Iguais")

#TODO 22
# a = int(input("Coloque um numero: "))
# b = int(input("Coloque outro numero: "))
# c = int(input("Coloque outro numero: "))

# lista = [a, b, c]
# if a != b and b != c and c != a:
#     print(sorted(lista))
# else: print("Numeros Iguais")

#TODO 23
# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# if nota1 > 10 or nota2 > 10:
#     print("Nota(s) Maior que a permitida")

# media = (nota1 + nota2) / 2
# conceitos = ['A', 'B', 'C', 'D', 'E']

# if media > 9 and media <= 10:
#     conceito = conceitos[0]
# elif media > 7.5 and media <= 9:
#     conceito = conceitos[1]
# elif media > 6 and media <= 7.5:
#     conceito = conceitos[2]
# elif media > 4 and media <= 6:
#     conceito = conceitos[3]
# else: conceito = conceitos[4]
# print(conceito)

# if conceito == "A" or conceito == "B" or conceito == "C":
#     print(f"\033[32m APROVADO, {nota1}, {nota2}, {media}, {conceito}")
# else: print(f"\033[31m REPROVADO, {nota1}, {nota2}, {media}, {conceito}")

#TODO 24
# valor1 = float(input("Valor 1: "))
# valor2 = float(input("Valor 2: "))

# # print("Escolha uma ação: \n Adição + \n Subtração - \n Multiplicação * \n Divisão /")
# a = int(input("Escolha uma ação: \n 1 Adição + | 2 Subtração - | 3 Multiplicação * | 4 Divisão / \n"))

# if a > 4:
#     print("Não tem essa operação")
# elif a == 1:
#     print(valor1 + valor2)
# elif a == 2:
#     print(valor1 - valor2)
# elif a == 3:
#     print(valor1 * valor2)
# else: print(valor1 / valor2)

#TODO 25
a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta = math.sqrt(b ** 2 - 4 * a *c)
if delta < 0:
    print("Não possui raiz")
elif delta == 0:
    x = -b + delta
    print(f"Existe um x real {x}")
else: x1 = -b + delta
x2 = -b - delta
print(f"Existe duas raizes {x1} e {x2}")