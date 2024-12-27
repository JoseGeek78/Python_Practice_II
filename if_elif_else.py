edad = int(input('Introduzca su edad:\n'))

# Se deja la variable sin valor.
respuesta = None

# Se evalúa si el usuario es mayor de edad. Si lo es, accede 
# a la compra de alcohol.
if edad >= 18:
    print('Es mayor de edad, puede comprar alcohol. ¿Cuál desea? Inroduzca un número de opción')
    respuesta = input('1- ron.\n2- whisky\3- ginebra.\n')
    
    if respuesta == '1':
        print('Ha elegido comprar ron')



# numero = 7

# if numero > 7:
#     print('El número es mayor que 7.')
# elif numero == 7:
#     print('El número es igual a 7.')
# else:
#     print('El número es menor o igual a 7.')