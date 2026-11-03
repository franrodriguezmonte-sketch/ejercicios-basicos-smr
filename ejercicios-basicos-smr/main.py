import time
import random

def pedir_numero(texto):
    while True:
        try:
            return float(input(texto).replace(",", "."))
        except ValueError:
            print("Eso no es un número válido, inténtalo de nuevo.")


def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Introduce un número entero.")


def fmt(n):
    return str(int(n)) if n == int(n) else str(round(n, 2))



def ejercicio_1():
    nombre = input("Introduce tu nombre: ")
    print(f"\nHola, {nombre}.")


def ejercicio_2():
    a = pedir_numero("Introduce el primer número: ")
    b = pedir_numero("Introduce el segundo número: ")
    print()
    print(f"Suma: {fmt(a + b)}")
    print(f"Resta: {fmt(a - b)}")
    print(f"Multiplicación: {fmt(a * b)}")
    if b == 0:
        print("División: no se puede dividir entre cero")
    else:
        print(f"División: {fmt(a / b)}")


def ejercicio_3():
    base = pedir_numero("Base: ")
    altura = pedir_numero("Altura: ")
    print(f"\nEl área del rectángulo es: {fmt(base * altura)}")


def ejercicio_4():
    celsius = pedir_numero("Temperatura en Celsius: ")
    fahrenheit = celsius * 9 / 5 + 32
    print(f"\n{fmt(celsius)} ºC equivalen a {fmt(fahrenheit)} ºF")


def ejercicio_5():
    nombre = input("Nombre: ")
    edad = pedir_entero("Edad: ")
    ciudad = input("Ciudad: ")
    print(f"\nHola, me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

def ejercicio_6():
    edad = pedir_entero("Introduce tu edad: ")
    if edad >= 18:
        print("\nEres mayor de edad.")
    else:
        print("\nEres menor de edad.")


def ejercicio_7():
    n = pedir_numero("Introduce un número: ")
    if n > 0:
        print("\nEl número es positivo.")
    elif n < 0:
        print("\nEl número es negativo.")
    else:
        print("\nEl número es cero.")


def ejercicio_8():
    n = pedir_entero("Introduce un número: ")
    if n % 2 == 0:
        print("\nEl número es par.")
    else:
        print("\nEl número es impar.")


def ejercicio_9():
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    if a > b:
        print(f"\nEl número mayor es {fmt(a)}.")
    elif b > a:
        print(f"\nEl número mayor es {fmt(b)}.")
    else:
        print("\nLos dos números son iguales.")


def ejercicio_10():
    nota = pedir_numero("Introduce tu nota (0-10): ")
    print()
    if nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
    elif nota < 5:
        print("Suspenso")
    elif nota < 7:
        print("Aprobado")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")


def ejercicio_11():
    precio = pedir_numero("Precio: ")
    print()
    if precio > 100:
        final = precio * 0.90
        print("Se aplica un descuento del 10 %.")
    else:
        final = precio
        print("No se aplica ningún descuento.")
    print(f"Precio final: {fmt(final)} €")

def ejercicio_12():
    contrasena_correcta = "1234"
    intento = input("Introduce la contraseña: ")
    if intento == contrasena_correcta:
        print("\nAcceso permitido.")
    else:
        print("\nContraseña incorrecta.")


def ejercicio_13():
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    op = input("Operación (+, -, *, /): ").strip()
    print()
    if op == "+":
        print(f"Resultado: {fmt(a + b)}")
    elif op == "-":
        print(f"Resultado: {fmt(a - b)}")
    elif op == "*":
        print(f"Resultado: {fmt(a * b)}")
    elif op == "/":
        if b == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            print(f"Resultado: {fmt(a / b)}")
    else:
        print("Operación no válida.")


def ejercicio_14():
    color = input("Color (rojo, amarillo, verde): ").strip().lower()
    mensajes = {
        "rojo": "Debes detenerte.",
        "amarillo": "Precaución, prepárate para detenerte.",
        "verde": "Puedes avanzar.",
    }
    print()
    print(mensajes.get(color, "El color no es válido."))


def ejercicio_15():
    meses = [
        ("Enero", 31), ("Febrero", 28), ("Marzo", 31), ("Abril", 30),
        ("Mayo", 31), ("Junio", 30), ("Julio", 31), ("Agosto", 31),
        ("Septiembre", 30), ("Octubre", 31), ("Noviembre", 30), ("Diciembre", 31),
    ]
    n = pedir_entero("Introduce el número del mes: ")
    print()
    if 1 <= n <= 12:
        nombre, dias = meses[n - 1]
        print(f"{nombre} tiene {dias} días.")
    else:
        print("El mes debe estar entre 1 y 12.")


def ejercicio_16():
    saldo = 1000.0
    while True:
        print("\n1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("\nElige una opción: ").strip()

        if opcion == "1":
            print(f"Saldo actual: {fmt(saldo)} €")
        elif opcion == "2":
            cantidad = pedir_numero("Cantidad a ingresar: ")
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            else:
                saldo += cantidad
                print("Ingreso realizado correctamente.")
                print(f"Saldo actual: {fmt(saldo)} €")
        elif opcion == "3":
            cantidad = pedir_numero("Cantidad a retirar: ")
            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
            elif cantidad > saldo:
                print("No tienes saldo suficiente.")
            else:
                saldo -= cantidad
                print("Retirada realizada correctamente.")
                print(f"Saldo actual: {fmt(saldo)} €")
        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


def ejercicio_17():
    importe = pedir_numero("Importe de la compra: ")
    if importe < 50:
        envio = 5
    elif importe < 100:
        envio = 2
    else:
        envio = 0
    print()
    print(f"Precio de la compra: {fmt(importe)} €")
    print(f"Gastos de envío: {fmt(envio) + ' €' if envio else 'Gratis'}")
    print(f"Total: {fmt(importe + envio)} €")


def ejercicio_18():
    edad = pedir_entero("Edad: ")
    print()
    if edad < 0:
        print("La edad no puede ser negativa.")
    elif edad < 5:
        print("Precio de la entrada: Gratis")
    elif edad <= 17:
        print("Precio de la entrada: 5 €")
    elif edad <= 64:
        print("Precio de la entrada: 10 €")
    else:
        print("Precio de la entrada: 6 €")


def ejercicio_19():
    tiempos = [pedir_numero(f"Tiempo corredor {i}: ") for i in range(1, 4)]
    mejor = min(tiempos)
    ganadores = [i + 1 for i, t in enumerate(tiempos) if t == mejor]
    print()
    for i, t in enumerate(tiempos, start=1):
        print(f"Corredor {i}: {fmt(t)}")
    if len(ganadores) > 1:
        lista = " y ".join(f"Corredor {g}" for g in ganadores)
        print(f"\nHay empate entre: {lista}")
    else:
        print(f"\nGanador: Corredor {ganadores[0]}")


def ejercicio_20():
    a = pedir_numero("Lado 1: ")
    b = pedir_numero("Lado 2: ")
    c = pedir_numero("Lado 3: ")
    print()
    if a == b == c:
        print("El triángulo es equilátero.")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")


def ejercicio_21():
    bruto = pedir_numero("Sueldo bruto: ")
    if bruto < 1000:
        porcentaje = 0
    elif bruto <= 2000:
        porcentaje = 10
    else:
        porcentaje = 20
    descuento = bruto * porcentaje / 100
    print()
    print(f"Sueldo bruto: {fmt(bruto)} €")
    print(f"Impuesto: {porcentaje} %")
    print(f"Descuento: {fmt(descuento)} €")
    print(f"Sueldo neto: {fmt(bruto - descuento)} €")


def ejercicio_22():
    a = pedir_numero("Número 1: ")
    b = pedir_numero("Número 2: ")
    c = pedir_numero("Número 3: ")
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    print(f"\nOrden: {fmt(a)} - {fmt(b)} - {fmt(c)}")


def ejercicio_23():
    total = pedir_entero("Introduce los segundos: ")
    horas = total // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60
    print()
    print(f"{horas} {'hora' if horas == 1 else 'horas'}")
    print(f"{minutos} {'minuto' if minutos == 1 else 'minutos'}")
    print(f"{segundos} {'segundo' if segundos == 1 else 'segundos'}")


def ejercicio_24():
    secreto = random.randint(1, 100)
    intentos_max = 3
    for intento in range(1, intentos_max + 1):
        n = pedir_entero(f"Adivina el número (intento {intento}/{intentos_max}): ")
        if n == secreto:
            print("\n¡Has acertado!")
            return
        elif n > secreto:
            print("El número secreto es menor.")
        else:
            print("El número secreto es mayor.")
    print(f"\nSe acabaron los intentos. El número era {secreto}.")


def ejercicio_25():
    producto = input("Producto: ")
    precio = pedir_numero("Precio: ")
    cantidad = pedir_entero("Cantidad: ")
    subtotal = precio * cantidad
    iva = subtotal * 0.21
    print()
    print(f"Producto: {producto}")
    print(f"Subtotal: {subtotal:.2f} €")
    print(f"IVA (21 %): {iva:.2f} €")
    print(f"Total: {subtotal + iva:.2f} €")

def ejercicio_26():
    anio = pedir_entero("Introduce un año: ")
    print()
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"{anio} → Año bisiesto")
    else:
        print(f"{anio} → No es bisiesto")


def ejercicio_27():
    importe = pedir_numero("Importe de la compra: ")
    descuento_pct = 0
    if importe > 500:
        respuesta = input("¿Tienes tarjeta de cliente? (s/n): ").strip().lower()
        descuento_pct = 15 if respuesta == "s" else 5
    descuento = importe * descuento_pct / 100
    print()
    print(f"Precio original: {fmt(importe)} €")
    print(f"Descuento ({descuento_pct} %): {fmt(descuento)} €")
    print(f"Precio final: {fmt(importe - descuento)} €")


def ejercicio_28():
    cantidad = pedir_entero("Cantidad a retirar (€): ")
    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        return
    print()
    restante = cantidad
    for billete in (50, 20, 10, 5):
        cuantos = restante // billete
        restante = restante % billete
        if cuantos > 0:
            print(f"{cuantos} {'billete' if cuantos == 1 else 'billetes'} de {billete} €")
    if restante > 0:
        print(f"No se pueden entregar {restante} € con billetes de 5 € o más.")


def ejercicio_29():
    n = pedir_entero("Número de dos cifras: ")
    n = abs(n)
    if not 10 <= n <= 99:
        print("\nEl número debe tener dos cifras.")
        return
    decenas = n // 10
    unidades = n % 10
    print(f"\nDecenas: {decenas}")
    print(f"Unidades: {unidades}")
    print(f"Suma: {decenas + unidades}")


def ejercicio_30():
    preguntas = [
        ("¿Cuánto es 5 + 3?", "8"),
        ("¿Cuál es la capital de España?", "madrid"),
        ("¿Cuántos días tiene una semana?", "7"),
        ("¿De qué color es el cielo en un día despejado?", "azul"),
        ("¿Cuánto es 9 x 3?", "27"),
    ]
    puntos = 0
    for pregunta, correcta in preguntas:
        print(f"\n{pregunta}")
        respuesta = input().strip().lower()
        if respuesta == correcta:
            print("¡Correcto!")
            puntos += 1
        else:
            print(f"Incorrecto. La respuesta era: {correcta}")
    print(f"\nPuntuación final: {puntos}/{len(preguntas)}")
EJERCICIOS = {
    1: ("Hola, usuario", ejercicio_1),
    2: ("Suma de dos números", ejercicio_2),
    3: ("Área de un rectángulo", ejercicio_3),
    4: ("Conversor de grados", ejercicio_4),
    5: ("Datos personales", ejercicio_5),
    6: ("Mayor de edad", ejercicio_6),
    7: ("Positivo, negativo o cero", ejercicio_7),
    8: ("Par o impar", ejercicio_8),
    9: ("El mayor de dos números", ejercicio_9),
    10: ("Nota del alumno", ejercicio_10),
    11: ("Descuento", ejercicio_11),
    12: ("Contraseña correcta", ejercicio_12),
    13: ("Calculadora básica", ejercicio_13),
    14: ("Semáforo", ejercicio_14),
    15: ("Días del mes", ejercicio_15),
    16: ("Cajero automático", ejercicio_16),
    17: ("Compra con gastos de envío", ejercicio_17),
    18: ("Precio de una entrada", ejercicio_18),
    19: ("Carrera", ejercicio_19),
    20: ("Tipo de triángulo", ejercicio_20),
    21: ("Calculadora de sueldo", ejercicio_21),
    22: ("Ordenar tres números", ejercicio_22),
    23: ("Conversor de segundos", ejercicio_23),
    24: ("Número secreto", ejercicio_24),
    25: ("Factura", ejercicio_25),
    26: ("Año bisiesto", ejercicio_26),
    27: ("Tarjeta de crédito", ejercicio_27),
    28: ("Cajero con billetes", ejercicio_28),
    29: ("Número de dos cifras", ejercicio_29),
    30: ("Mini test", ejercicio_30),
}


def mostrar_menu():
    print("\n" + "=" * 40)
    print("   EJERCICIOS DE PROGRAMACIÓN")
    print("=" * 40)
    for numero, (titulo, _) in EJERCICIOS.items():
        print(f"{numero:>2}. {titulo}")
    print(" 0. Salir")


def main():
    while True:
        mostrar_menu()
        eleccion = input("\nElige un ejercicio: ").strip()
        if eleccion == "0":
            print("¡Hasta luego!")
            break
        if eleccion.isdigit() and int(eleccion) in EJERCICIOS:
            titulo, funcion = EJERCICIOS[int(eleccion)]
            print(f"\n--- Ejercicio {eleccion}: {titulo} ---\n")
            funcion()
        else:
            print("Opción no válida. Elige un número del 0 al 30.")


if __name__ == "__main__":
    main()