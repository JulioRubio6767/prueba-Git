def sumar(*num):
    return sum(num)

# Pedir la cantidad de números a ingresar
cantidad = int(input("¿Cuántos números desea ingresar? "))

valores = []
for i in range(cantidad):
    digito = int(input(f"Ingrese el número {i + 1}: "))
    valores.append(digito)  # ✅ Agregar el número ingresado

# Llamar a la función con los valores desempaquetados
print(f"Al sumar los {cantidad} numeros es:", sumar(*valores))
