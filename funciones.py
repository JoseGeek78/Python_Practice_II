# Definimos funciones para cada operación matemática:
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede divivir por cero."
    return a / b

#Función principal que muestra en el menú y obtiene la entrada del usuario
def calculadora():
    while True:
        print("Seleccione una operación:\n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora.")
            break
        
        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Ingrese valores numérocos válidos.")
                continue
            
            if opcion == '1':
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida, inténtelo de nuevo.")
            
# Llamamos a la función principal para ejecutar la calculadora
calculadora()



#nombres = ['Jose', 'Jimena', 'Natalia']

#def añadir_names(names):
#    nombres.insert(0, names)
    
#añadir_names(input('Esriba un nombre para añadir a la lista:\n'))

#print(nombres)

#animales = ['perro', 'gato', 'lobo']

#def añadir_animals(animals):
#    animales.insert(0, animals)

#añadir_animals(input('Escriba un animal para añadir a la lista:\n'))

#print(animales)

#colores = ['rojo', 'verde', 'amarillo']

#def añadir_color(color):
#    colores.insert(0, color)
    
#añadir_color(input('Escriba un color para añadirlo a la lista:\n'))

#print(colores)

#transporte = ['bicicleta', 'autobús', 'coche']

#def añadir_transport(transport):
#    transporte.insert(0, transport)
    
#añadir_transport(input('Escriba un medio de transporte para añadirlo a la lista:\n'))

#print(transporte)

#def suma(numero1,numero2):
#    return numero1 + numero2
#
#resultado1 = suma(225, 58)
#resultado2 = suma(98, 785)

#suma_sumas = resultado1 + resultado2

#print(suma_sumas)


#def suma(numero1,numero2):
#    return numero1 + numero2
    
#resultado = suma(5289553, 484545)

#print(resultado)

#def resta(numero1,numero2):
#    return numero1 - numero2

#resultado2 = resta(5689, 985)

#print(resultado2)

#def multiplicacion(numero1,numero2):
#    return numero1 * numero2

#resultado3 = multiplicacion(56948,2569878)

#print(resultado3)

#def division(numero1,numero2):
#    return numero1 / numero2

#resultado4 = division(589654,256)

#print(resultado4)


# def saludar(nombre, edad):
#     print(f'!Hola {nombre}!')
#     print(f'Tú tienes {edad} años.')
    
# saludar('Jose', 46)
# saludar('Sergio', 26)
# saludar('Fran', 23)
# saludar('Vane', 37)
