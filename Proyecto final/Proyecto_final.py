#Datos del usuario
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tus apellidos: ")
edad = int(input("Introduce tu edad: "))
peso = float(input("Introduce tu peso en kilogramos: "))
estatura = float(input("Introduce tu estatura en metros: "))

print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Edad: " + str(edad) + " años")
print("Peso: " + str(peso) + " kg") 
print("Estatura: " + str(estatura) + " m")

#Desarrollo del IMC
#Fórmula peso / estatura**2
indice = float(peso / estatura * 2)

if indice >= 0 and indice <= 18.5 :
    print("Peso Bajo")
if indice >= 18.50 and indice <= 24.99 :
    print("Peso normal")
if indice >= 25.00 and indice <= 29.99 :
    print("Sobre peso")
if indice >= 30.00 and indice <= 34.99 :
    print("Obesidad leve")
if indice >= 35.00 and indice <= 39.99 :
    print("Obesidad media")
if indice >= 40.00 :
    print("Obesidad morbida")