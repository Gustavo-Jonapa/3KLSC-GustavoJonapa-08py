MaxTamC = 10
A = [0] * MaxTamC
frente = 0
final = 0
contador = 0

# Iniciar la cola
respuesta = input("¿Desea agregar elemento a la cola?(s/n): ").lower()

while respuesta == 's' and contador < MaxTamC:
    # Verificar desbordamiento
    if (final + 1) % MaxTamC == frente:
        print("Desbordamiento de la cola")
        break  # Usar break en vez de exit para continuar el flujo

    elemento = int(input("Ingrese un elemento para la cola: "))
    final = (final + 1) % MaxTamC
    A[final] = elemento

    contador += 1
    print(f"Elemento {contador} agregado a la cola: {elemento}")

    # Preguntar si desea agregar más elementos
    if contador < MaxTamC:
        respuesta = input("¿Desea agregar más elementos a la cola?(s/n): ").lower()

# Validar si la cola está vacía antes de eliminar
if frente == final:
    print("La cola está vacía.")
else:
    # Obtener el primer elemento de la cola
    primerElemento = A[(frente + 1) % MaxTamC]
    print(f"El primer elemento de la cola es: {primerElemento}")

    # Eliminar un elemento de la cola
    frente = (frente + 1) % MaxTamC

# Imprimir elementos de la cola en el orden en que fueron ingresados
print("Elementos de la cola en el orden de ingreso:")
i = (frente + 1) % MaxTamC
while i != (final + 1) % MaxTamC:
    print(A[i], end=" ")
    i = (i + 1) % MaxTamC
print()

