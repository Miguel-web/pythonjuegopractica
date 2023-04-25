name = "Miguel"
age = 37
lastname ="Gil"

# box = ["Hola"]

# imprime el nombre o la variable
#print (name)

# print (type(age))

# tipos de datos: 
# 1- Enteros int()
# 2- decimal float()
# 3- String str()
# 4- Enteros Bool()

# operadores logicos : 
# and : ambas tienen que ser verdaderas
# or , 
# not

# condicionales
# if 
# else

# if name == "Miguel" and lastname == "Gil":
#     print("Verdadero")

# if name == "Miguel" or lastname == "Gil":
#     print("Verdadero")

# if age < 18:
#     print("Puede ver la pelicula")
# else:
#     print("No puede ver la pelicula")

# loop
lista = [Miguel, 16, True]

counter = 0

while True:
    print(counter)
counter = counter +1    
if counter >= 10:
    break

for cosas in lista:
    print(cosas)

print("*" * 20)

# clase de deimian python intro worckshop y juego

name = "Deimian"
age = 25
hombre = True
lastname = "Vásquez"


# name = "Vásquez"

# imprime el nombre
# print(type(name))
# print(type(age))
# print(type(hombre))

#tipos de datos
# int -> enteros
# float -> decimales
# string -> cadenas de texto   -> str
# bool -> verdadero o falso


# operadores logicos 
# and  -> ambas partes deben ser verdaderas 
# or  -> si una es verdadera todo es verdadero 
# not  -> negación




#condicionales 
#if
#else

# age = 65

# if age > 64:
#    print("Puede ver la pelicula y tiene un descuento")
# elif age > 18:
#   print("Puede ver la pelicula")
# else:
#   print("no puede ver la pelicula")

# loop 
# lista = ["Deimian", 16, True]

# counter = 0
# while counter <= len(lista)-1: 
#   print(lista[counter])
#   counter += 1


# print("*" * 20)

# for cosas in lista:
#   print(cosas)


# def sum(num1, num2):
#   return num1 + num2

# print(sum(50, 50))

# message = input("Escribe un mensaje: ")

# print(message)


# Juego usando Python Muerto y Herido !!!

import random
# 1- Cuando el juego arranca la máquina debe elgir un número entre 0 - 9
# 2- Debe perdir al usuario que ingrese un número de tres dígitos, se lo pide por la terminal
# 3 - Si se acierta el número pero no la posición cuenta como un herido
# 4 - Si acierta posición y número cuenta como un muerto
# 4 - si tiene tres muertos gana



lista_numeros = [0,1,2,3,4,5,6,7,8,9]
seleccion_maquina = random.sample(lista_numeros, 3)

while True:
  muerto = 0
  herido = 0


  entrada_usuario = input("Ingresa un número de tres dígitos: ")

  if len(entrada_usuario) != 3:
    print("El número que ingresaste debe tener tres dígitos manito")
    continue

  seleccion_usuario = []

  for num in entrada_usuario:
    seleccion_usuario.append(int(num))
  
  for index_maquina, valor_maquina in enumerate(seleccion_maquina):
    for index_usario, valor_usuario in enumerate(seleccion_usuario):
      if index_maquina == index_usario and valor_maquina == valor_usuario:
        muerto = muerto + 1
      elif valor_usuario == valor_maquina:
        herido = herido +1

  if muerto == 3:
    print("Eeeeeeeeeeeeeeee ganastesssssss")
    break

  print(f"Tienes {muerto} muerto y {herido} heridos\n\n")

