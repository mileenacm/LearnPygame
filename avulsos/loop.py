#tabuada do 7 usando for
#for seven in range(1,11):
   # print(f" 7 x {seven} = {seven * 7} ")

#number = int(input("Qual a tabuda desejada? "))

#for j in range(1,11):
   # print(f" {number} x {j} = {number * j}")

#for j in range(1,7):
    
   # print("*" * j)

#days_week = ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]
'''weekend = ("Satur", "Sun")
for days in days_week:
    if days in weekend:
        continue
    print(days)

emails = (" damon@gmail.com ", 'elena@outlook.br', 'SQL injection;', 'nano.banana@gemini.ai')

for email in emails:
    email = email.strip()
    if ';' in email:
        print("Hacker Attack!")
        break
    print(email)

emails2 = [ "damon@gmail.com", 'elena@outlook.br', 'nano.banana@gemini.ai', None]

print( )

for email in emails2:
    if email is None:
        print("Found missing emails!")
        break
else:
    print("No missing emails")'''


''''files = ["vampire.csv", "blood.csv", "fangs.txt", 'powers.pdf']

for file in files:
    if not file.endswith('.csv'):
        print(f"Not all files are CSV: {file}")
        break

else:
    print("All files are CSV!")'''

'''file_list = [ 'summary.docx', 'report.csv', 'data.csv', 'data.xlsx', 'data.xlsx','report.csv', ]


#usar argumento set pra comparar o tamanho da original com a lista de valores unicos

if len(file_list) != len(set(file_list)):
    print(f"Duplicate exist!")

print( ) 

duplicatas = []

for i in file_list:

    if duplicatas.count(i) > 1 and i not in duplicatas:
        duplicatas.append(i)
print("duplicados: ", duplicatas)







#como eu percorro a lista e comparo se os itens são iguais?
duplicados = []

for item in file_list:
    if file_list.count(item) > 1 and item not in duplicados:
        duplicados.append(item)

print("duplicatas:", duplicados) '''

#nested loops
'''
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"({x},{y},{z})")

#serve para cmbinar dados e encontrar as possibilidades de cruzamento, tipo a arvore no pfc
colors = ['red', 'blue', 'green']
sizes = ['L', "M", 'S']
for color in colors:
    for size in sizes:
        print(f"{color} - size {size}")

#navegar entre hierarquias
years = [2026, 2027]
months = ['Jan','Feb']
days = range(1,11)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}")


#navegar entre tabelas e colunas: cada coluna tem sua linha, automatizar 
tables = ['costumers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL;")'''

# WHILE

#condition e True 

'''ask = ""

while ask != 'yes':
    ask = input("Do you agree? ")
print("Thanks for answering")'''

'''# o tipo precisa ter uma condição de parada
i = 3
while i < 4:
    ask = input(f"Do you agree? Only {i} attempts: ")
    i -= 1
    if i == 0:
        print("NO chances anymore.")
        break
    if ask == 'yes':
        print("Glad we are on the same page here")
        break'''
'''
print(abs(2 - 10)) #valor absoluto, distancia, tamanho
# no metodo round()
price = 14.54839
price = 12.53211
price = 0.56
print(round(price))

import math

price = 0.455
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price))

print()
import random
#print(random.random())
print(random.randint(1,6))

print( )
#validaçao
x = 3.4
print(x.is_integer())

print()
y = 40
print(isinstance(y, complex))
'''

import random

y = random.randint(1,100)
print(y)

if y % 2 == 0:
    print("Even number!")
else:
    print("Odd number!")

booleanos = [True, False, True]
print(any(booleanos)) 

booleanos = [True, False, True]
print(all(booleanos)) 


print(bool(booleanos))

#x is y compara os ids das variaveis    

costs = [20,3,20,1,50,34]
print(sum(costs))
print(min(costs))
print(max(costs))
