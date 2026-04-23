import random

letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!#$%&/@"
todos = letras + numeros + simbolos

nombre_usuario = input("Ingrese su nombre de usuario: ")

password = ""
for i in range (8):
    password = password + random.choice(todos)


print(nombre_usuario+", "+"tu nuevo password es: "+ password)
