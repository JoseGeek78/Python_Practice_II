error = input('Introduzca un código de error\n')

if error == '200':
    print('Todo ok.')
elif error == '301':
    print('Movimiento permanente de la página.')
elif error == '302':
    print('Movimiento temporal de la página.')


# error = input('Introduzca un código de error:\n')

# match error:
#     case '200':
#         print('Todo ok.')
#     case '301':
#         print('Movimiento permanente de la página.')
#     case '302':
#         print('Movimiento temporal de la página.')
#     case '404':
#         print('Página no encontrada.')
#     case '500':
#         print('Error interno del servidor.')
#     case '503':
#         print('Servicio no disponible.')
#     case defecto:
#         print('Error no disponible.')

# color = 'azul'
# forma = 'cuadrado'
# forma = 'cuadrado'
# tamaño = 'grande'
# tamaño = 'grande'

# if (color == 'rojo' and forma == 'círculo' and tamaño == 'pequeño'):
#     print('Es un cuadrado azul.')

# if not(color == 'rojo' and forma == 'círculo' and tamaño == 'pequeño'):
#     print('Es un cuadrado azul.')
# else:
#    print('No se cumple la condición.')


# edad = int(input('Introduzca su edad:\n'))

# # Se deja la variable sin valor.
# respuesta = None

# # Se evalúa si el usuario es mayor de edad. Si lo es, accede 
# # a la compra de alcohol.
# if edad >= 18:
#     # Mensaje indicando que el usuario puede comprar alcohol.
#     print('Es mayor de edad, puede comprar alcohol. ¿Cuál desea? Inroduzca un número de opción')
#     # Se pide al usuario que seleccione una opción.
#     respuesta = input('1- ron.\n2- whisky\n183- ginebra.\n')
    
#     # Se evalúa la respuesta ingresada por el usuario.
#     if respuesta == '1':
#         # Mensaje para la opción de ron.
#         print('Ha elegido comprar ron.')
#     elif respuesta == '2':
#         # Mensaje para la opción de whisky.
#         print('Ha elegido comprar whisky.')
#     elif respuesta == '3':
#         # Mensaje para la opción de ginebra.
#         print('Ha elegido comprar ginebra.')
#     else:
#         # Mensaje si la opción ingresada no es válida.
#         print('Opción no válida.')
# else:
#     # Mensaje para menores de edad.
#     print('Es menor de edad, vuelva de aquí a un tiempo o no empiece con el alcohol.')


# numero = 7

# if numero > 7:
#     print('El número es mayor que 7.')
# elif numero == 7:
#     print('El número es igual a 7.')
# else:
#     print('El número es menor o igual a 7.')