colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Naranja', 'Rosa']

print('---LISTADO DE COLORES---')

for color in colores:
    if color == 'Azul' or color == 'Amarillo':
        print('Se ha saltado este color.')
        continue
    print(f'-Color {color}.')



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