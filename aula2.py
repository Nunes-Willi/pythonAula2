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
idade = int(input("Sua idade: "))
if idade >= 18 and idade < 65:
    print("Você é de Maior")
elif idade < 18:
    print("Você é DMenor")
else: print("Acima de 65 anos")