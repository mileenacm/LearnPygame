# listas: str, number or both and mixed
letter = list('DATA')
print(letter)

number = list(range(1,11,1))
print(number)
print()

#nested list = matrix


matrix = [['a','b','c'], ['d','e','f']] # 2 rows , pode ser mixed também

#como acessar valores: indexação e fatiamento

print(len(letter))

'''primeiro e ultimo item'''
print(letter[0])
print(letter[4-1]) # o tamanho da lista é 4 mas o ultimo item fica na posição j - 1, ou seja, 3
# ou da direita para a esquerda: -4, -3, -2, -1
print(letter[-2])

#agora acessar matrizes

#Baraa usa analogia de ir ao cinema, row and seat
#navegamos pela matriz primeiro pela linha row, depois a coluna
# matrix, a lista inteira
#matriz[j], uma linha
#matriz[j][i], um item
#matriz[-1][-1], ultimo item

#slicing: pegar dois itens, preciso dizer o start e o end

print(letter[0:3])
print(letter[2:])
print(letter[:])
print(letter[:3])

print(matrix[0:1])
print(matrix[1:])
print(matrix[:2])

print(matrix[1][:2])

#packing: colocar item
#unpacking: retirar

person = ['maria', 29, 'data engineer', 'spain']

#unpacking
#name, age, role, country = person
name, *details, country = person
print(name)
print(details)
print(country)

*details, country = person
print(details)
print(country)

print( )

#first, *rest = number != first, rest = number

# agora com underscore '_', skips items
name, _, role, _ = person
print(name, role)

first, *_, last = person
print(first, last)


#how to explore and analyse, insert,remove,append,pop
letter.remove('D')
print(letter)
letter.insert(1, 'x')
print(letter)
#letter.clear()
#print(letter)
letter.append('D')
print(letter)
letter.pop(1) #index
print(letter)


matrix.append(['a','b','c'])
matrix.insert(1,['a','b','c'])

matrix[0].append(['x','y','z']) 

#matrix[1].remove('string')
matrix[-1].pop(0)
matrix[0].pop()

#update

letter[1] = 'm'
letter = list('Armand')
print(letter)

matrix[1] = ['a','d','l']
matrix[0][1]= ['l','g','f']

letter1 = ['a','c','d','b']
#letter1.sort()
#letter1.sort(reverse = True)
print(letter1)


#matrix[i].sort() #the first item of each inner list

#sem modificar a lista original: .sorted(), cria uma copia extra. .sorted(reverse = True)

#letter1.reverse()
letter_new = reversed(letter1) 
#cria um objeto chamado iterador
#ou
letter_new = list(reversed(letter1)) #igual ao sorted

#shallow copy, afeta os valores da lista original e da copia, não sao independentes em um nivel profundo, só superficial
letter_copy =  letter1.copy() #flat list

import copy
#pra copiar camada por camada
letter_copy = letter1.deepcopy( ) #nested list
#copy.copy( ) is more general not limited to list
#Usar operador is pra saber se as copias sao mesmo independentes


#combine data

#comb = letters + numbers
#comb = [letters, numbers]
#print(letters * 2)
#numbers.extend(letters)

#pareando os itens com zip(), retorna uma lista de tuplas, pares
# se uma lista for maior que outra, itens vao sobrar e n vao ser pareados
#comb = zip(letter, numbers)
#comb = list(zip(letter, numbers, 'hi'))


#How to iterate

'''iterator = processing, machine'''
'''iterable = the thing, like a list'''

#enumerate(letter, start = 1)
#list(enumerate(letter, start = 1))
# for index, value in enumerate(letter):

#filter(None, letter)
#for i in filter(str.isalpha(), items ):
#   print(i)

#Função lambda

'''multiple = lambda x: x*2
print(multiple(2))

add = lambda x,y: x + y

check = lambda i: for i in "python" '''











