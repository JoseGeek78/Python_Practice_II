edad = int(input('Introduzca su edad:\n'))

# Se deja la variable sin valor.
respuesta = None

# Se evalúa si el usuario es mayor de edad. Si lo es, accede 
# a la compra de alcohol.
if edad >= 18:
    print('Es mayor de edad, puede comprar alcohol. ¿Cuál desea? Inroduzca un número de opción')
    respuesta = input('1- ron.\n2- whisky\n183- ginebra.\n')
    
    if respuesta == '1':
        print('Ha elegido comprar ron.')
    elif respuesta == '2':
        print('Ha elegido comprar whisky.')
    elif respuesta == '3':
        print('Ha elegido comprar ginebra.')
    else:
        print('Opción no válida.')
else:
    print('Es menor de edad, vuelva de aquí a un tiempo o no empiece con el alcohol.12')



# numero = 7

# if numero > 7:
#     print('El número es mayor que 7.')
# elif numero == 7:
#     print('El número es igual a 7.')
# else:
#     print('El número es menor o igual a 7.')