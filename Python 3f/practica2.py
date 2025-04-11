'''
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
'''
def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("No se puede dividir por cero")

division(2,1)
division(2,0)




'''

Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
'''
def sumar(a,b):
    try:
        print(a+b)
    except Exception as e:
        print(f"No corresponde el tipo de dato {e}")

sumar(2 + "hola")




""" Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra un error al usuario. """

dic = {"nombre": "kevin", "lenguaje": "python"}

try:
    print(dic[apellido])
except Exception as e:
    print(f"Esa llave no existe en el diccionario. {e}")


""" Escriba un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe. """

try:
    with open("archivo.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"El archivo no existe. {e}")
    with open("archivo.txt", "w") as f:
        f.write("Archivo creado")
        print("archivo creado")


""" Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario. """


try:
    print(2/0)
except Exception as e:
    print(f"No se puede dividir por cero. Error: {e}")