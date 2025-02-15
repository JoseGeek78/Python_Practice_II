lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

# Se ordena la lista de menor a mayor.
lista_numeros.sort()

# Bucle para iterar la lista.
for i in lista_numeros:
    if i == 10:
        continue # Se omiten los valores 10.
    elif i ==356:
        break # Se rompe la iteración, rompe la ejecución del bucle.
    else:
        print(f'El valor del elemento es: {i}.')


# Lista de países
# paises = [
#     "Argentina", "Australia", "Brasil", "Canadá", "China", "Colombia", "Egipto", "España", "Estados Unidos", 
#     "Francia", "India", "Indonesia", "Italia", "Japón", "México", "Nigeria", "Países Bajos", "Perú", 
#     "Polonia", "Portugal", "Reino Unido", "Rusia", "Sudáfrica", "Suecia", "Suiza", "Tailandia", "Turquía", 
#     "Ucrania", "Venezuela", "Vietnam"
# ]

# Bucle para recorrer la lista de países e imprimir cada uno
# for pais in paises:
#     print(f'-> {pais} <-')

# ---------------------------------------------

# Bucle que decrementa de 0 a -5000 en pasos de -500
# for i in range(0, -5001, -500):
#     print(f'El valor del bucle es {i}.')

# ---------------------------------------------

# Bucle while que incrementa desde 2 hasta 16 en pasos de 2
# i = 2
# while i <= 16:
#     print(f'El valor del bucle es: {i}.')
#     i += 2


# while i <= 16:
#    print(f'El valor del bucle es: {i}.')
#    i += 2


# colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Naranja', 'Rosa']

# print('---LISTADO DE COLORES---')

# for color in colores:
#     if color == 'Amarillo':
#         print('Se ha roto la ejecución del bucle.')
#         break
#     print(f'-Color {color}.')

# colores = ['Rojo', 'Azul', 'Verde', 'Amarillo']

# print('---LISTADO DE COLORES---')

# for color in colores:
#     print(f'-{color}.')

# for i in range(3,13,3):
#     print(f'El valor del bucle es: {i}.')

# print('Fin!')

# for i in range(3,8):
#     print(f'El valor del bucle es {i}.')
#     print(f'Contamos...')
    
# print('Fin del blucle.')

# for i in range(3,7):
#     print(f'El valor del bucle es {i}.')