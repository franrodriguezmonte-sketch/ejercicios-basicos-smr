# 🧑‍💻 Ejercicios de Programación

Colección de ejercicios para practicar los conceptos básicos de programación.

Los ejercicios están organizados por niveles de dificultad. Se recomienda realizarlos en orden.

---

# 🟢 Nivel 1 — Variables y entrada de datos

En este nivel trabajaremos con:

* Variables
* Entrada de datos
* Conversión de tipos
* Operaciones matemáticas
* Salida por pantalla

### 1. 👋 Hola, usuario

Pide el nombre del usuario y muestra un saludo.

**Ejemplo:**

```text
Introduce tu nombre: Ana

Hola, Ana.
```

---

### 2. ➕ Suma de dos números

Pide dos números y muestra:

* Su suma
* Su resta
* Su multiplicación
* Su división

**Ejemplo:**

```text
Introduce el primer número: 10
Introduce el segundo número: 2

Suma: 12
Resta: 8
Multiplicación: 20
División: 5
```

---

### 3. 📐 Área de un rectángulo

Pide la base y la altura de un rectángulo y calcula su área.

**Ejemplo:**

```text
Base: 5
Altura: 3

El área del rectángulo es: 15
```

---

### 4. 🌡️ Conversor de grados

Pide una temperatura en grados Celsius y conviértela a Fahrenheit.

**Fórmula:**

```text
Fahrenheit = Celsius × 9 / 5 + 32
```

**Ejemplo:**

```text
Temperatura en Celsius: 25

25 ºC equivalen a 77 ºF
```

---

### 5. 👤 Datos personales

Pide al usuario:

* Nombre
* Edad
* Ciudad

Después muestra una frase utilizando todos los datos.

**Ejemplo:**

```text
Nombre: Ana
Edad: 20
Ciudad: Vigo

Hola, me llamo Ana, tengo 20 años y vivo en Vigo.
```

---

# 🟡 Nivel 2 — Condicionales

En este nivel comenzaremos a tomar decisiones utilizando estructuras condicionales.

Trabajaremos con:

* `if`
* `else`
* `else if` / `elif`
* Operadores de comparación
* Operadores lógicos

---

### 6. 🎂 Mayor de edad

Pide la edad del usuario e indica si es mayor o menor de edad.

**Ejemplo:**

```text
Introduce tu edad: 17

Eres menor de edad.
```

---

### 7. 🔢 Número positivo, negativo o cero

Introduce un número y determina si es:

* Positivo
* Negativo
* Cero

**Ejemplo:**

```text
Introduce un número: -8

El número es negativo.
```

---

### 8. 🔢 Número par o impar

Pide un número e indica si es par o impar.

**Ejemplo:**

```text
Introduce un número: 7

El número es impar.
```

---

### 9. 🏆 El mayor de dos números

Pide dos números y muestra cuál de ellos es mayor.

También debes contemplar el caso en el que ambos números sean iguales.

**Ejemplo:**

```text
Primer número: 15
Segundo número: 8

El número mayor es 15.
```

---

### 10. 📝 Nota del alumno

Pide una nota entre 0 y 10 y muestra la calificación correspondiente:

| Nota    | Resultado     |
| ------- | ------------- |
| 0 - 4.9 | Suspenso      |
| 5 - 6.9 | Aprobado      |
| 7 - 8.9 | Notable       |
| 9 - 10  | Sobresaliente |

**Ejemplo:**

```text
Introduce tu nota: 8

Notable
```

---

### 11. 💰 Descuento

Pide el precio de un producto.

Si el producto cuesta **más de 100 €**, aplica un descuento del **10 %**.

En caso contrario, no se aplica ningún descuento.

**Ejemplo:**

```text
Precio: 150 €

Se aplica un descuento del 10 %.
Precio final: 135 €
```

---

# 🟠 Nivel 3 — Lógica y problemas

En este nivel los ejercicios requieren combinar varias operaciones y condiciones.

Se recomienda intentar resolverlos sin mirar soluciones y dividir cada problema en pequeños pasos.

---

### 12. 🔐 Contraseña correcta

Crea un programa que tenga una contraseña almacenada.

Pide al usuario que introduzca la contraseña.

* Si es correcta, muestra `Acceso permitido`.
* Si es incorrecta, muestra `Contraseña incorrecta`.

**Ejemplo:**

```text
Introduce la contraseña: 1234

Acceso permitido.
```

---

### 13. 🧮 Calculadora básica

Pide al usuario:

1. Un número.
2. Otro número.
3. Una operación (`+`, `-`, `*` o `/`).

El programa debe realizar la operación indicada.

También debe controlar que no se pueda dividir entre cero.

**Ejemplo:**

```text
Primer número: 10
Segundo número: 5
Operación: *

Resultado: 50
```

---

### 14. 🚦 Semáforo

Pide al usuario un color de semáforo:

* `rojo`
* `amarillo`
* `verde`

El programa debe mostrar qué debe hacer el peatón o conductor.

**Ejemplo:**

```text
Color: rojo

Debes detenerte.
```

Si se introduce un color que no existe, muestra un mensaje indicando que el color no es válido.

---

### 15. 📅 Días del mes

Pide al usuario un número correspondiente a un mes:

```text
1 = Enero
2 = Febrero
3 = Marzo
...
12 = Diciembre
```

Muestra el nombre del mes y cuántos días tiene.

Para simplificar el ejercicio, considera que febrero tiene siempre **28 días**.

**Ejemplo:**

```text
Introduce el número del mes: 4

Abril tiene 30 días.
```

---

### 16. 🏦 Cajero automático

Simula una operación sencilla de un cajero automático.

El usuario dispone inicialmente de **1.000 €**.

Muestra un menú:

```text
1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir
```

El programa debe:

* Mostrar el saldo.
* Permitir ingresar dinero.
* Permitir retirar dinero.
* No permitir retirar más dinero del disponible.
* Mostrar un mensaje al salir.

**Ejemplo:**

```text
1. Consultar saldo
2. Ingresar dinero
3. Retirar dinero
4. Salir

Elige una opción: 3

Cantidad a retirar: 200

Retirada realizada correctamente.
Saldo actual: 800 €
```

---

### 17. 🛒 Compra con gastos de envío

Una tienda online cobra gastos de envío dependiendo del importe de la compra:

| Importe              | Gastos de envío |
| -------------------- | --------------: |
| Menos de 50 €        |             5 € |
| Entre 50 € y 99.99 € |             2 € |
| 100 € o más          |          Gratis |

Pide el importe de la compra y muestra:

* El precio de la compra.
* Los gastos de envío.
* El precio total.

**Ejemplo:**

```text
Importe de la compra: 75 €

Gastos de envío: 2 €
Total: 77 €
```

---

### 18. 🎟️ Precio de una entrada

Calcula el precio de una entrada dependiendo de la edad:

* Menores de 5 años → Gratis.
* De 5 a 17 años → 5 €.
* De 18 a 64 años → 10 €.
* 65 años o más → 6 €.

Pide la edad y muestra el precio correspondiente.

**Ejemplo:**

```text
Edad: 70

Precio de la entrada: 6 €
```

---

### 19. 🏃 Carrera

Pide el tiempo realizado por tres corredores.

El programa debe mostrar:

* El tiempo del primer corredor.
* El tiempo del segundo corredor.
* El tiempo del tercer corredor.
* Quién ha ganado.
* Si existe empate.

**Ejemplo:**

```text
Tiempo corredor 1: 12.5
Tiempo corredor 2: 11.8
Tiempo corredor 3: 13.2

Ganador: Corredor 2
```

---

### 20. 🔺 Tipo de triángulo

Pide las longitudes de los tres lados de un triángulo.

Determina si es:

* Equilátero → los tres lados son iguales.
* Isósceles → dos lados son iguales.
* Escaleno → todos los lados son diferentes.

**Ejemplo:**

```text
Lado 1: 5
Lado 2: 5
Lado 3: 3

El triángulo es isósceles.
```

---

### 21. 🧮 Calculadora de sueldo

Pide el sueldo de una persona.

Calcula un impuesto dependiendo del salario:

* Menos de 1.000 € → 0 %.
* Entre 1.000 € y 2.000 € → 10 %.
* Más de 2.000 € → 20 %.

Muestra:

* Sueldo bruto.
* Porcentaje de impuesto.
* Cantidad descontada.
* Sueldo neto.

**Ejemplo:**

```text
Sueldo bruto: 1800 €

Impuesto: 10 %
Descuento: 180 €
Sueldo neto: 1620 €
```

---

### 22. 🔢 Ordenar tres números

Pide tres números diferentes y muestra los números ordenados de menor a mayor.

**Ejemplo:**

```text
Número 1: 8
Número 2: 3
Número 3: 5

Orden: 3 - 5 - 8
```

**Reto:** intenta resolverlo utilizando únicamente estructuras condicionales.

---

### 23. 🕐 Conversor de segundos

Pide una cantidad de segundos y conviértela a:

* Horas
* Minutos
* Segundos

**Ejemplo:**

```text
Introduce los segundos: 3672

1 hora
1 minuto
12 segundos
```

---

### 24. 🎯 Número secreto

El programa debe tener un número secreto almacenado.

El usuario debe introducir un número e indicar si ha acertado.

Si no acierta, el programa debe decir si el número introducido es:

* Mayor que el número secreto.
* Menor que el número secreto.

**Ejemplo:**

```text
Adivina el número: 50

El número secreto es menor.
```

**Reto:** añade tres intentos como máximo.

---

### 25. 🧾 Factura

Crea un programa que pida:

* Nombre del producto.
* Precio.
* Cantidad.

Calcula:

* Precio total sin IVA.
* IVA del 21 %.
* Precio final.

**Ejemplo:**

```text
Producto: Teclado
Precio: 30 €
Cantidad: 2

Subtotal: 60 €
IVA: 12.60 €
Total: 72.60 €
```

---

## ⭐ Retos adicionales

Estos ejercicios son opcionales para aquellos alumnos que quieran practicar un poco más.

### 26. 🗓️ Año bisiesto

Pide un año y determina si es bisiesto.

Un año es bisiesto si:

* Es divisible entre 4.
* Pero los años divisibles entre 100 no son bisiestos, salvo que también sean divisibles entre 400.

**Ejemplos:**

```text
2024 → Año bisiesto
2023 → No es bisiesto
1900 → No es bisiesto
2000 → Año bisiesto
```

---

### 27. 💳 Tarjeta de crédito

Pide el importe de una compra.

Si el importe es superior a 500 €, pregunta si el usuario tiene tarjeta de cliente.

* Si tiene tarjeta, aplica un 15 % de descuento.
* Si no tiene tarjeta, aplica un 5 %.
* Si la compra es de 500 € o menos, no aplica descuento.

Muestra el precio original, el descuento y el precio final.

---

### 28. 🏧 Cajero con billetes

Pide una cantidad de dinero que el usuario quiere retirar.

El programa debe indicar cuántos billetes de:

* 50 €
* 20 €
* 10 €
* 5 €

debe entregar.

Intenta utilizar el menor número posible de billetes.

**Ejemplo:**

```text
Cantidad: 135 €

2 billetes de 50 €
1 billete de 20 €
1 billete de 10 €
1 billete de 5 €
```

---

### 29. 🔢 Número de dos cifras

Pide un número de dos cifras y muestra:

* Sus unidades.
* Sus decenas.
* La suma de ambas cifras.

**Ejemplo:**

```text
Número: 47

Decenas: 4
Unidades: 7
Suma: 11
```

---

### 30. 🧠 Mini test

Crea un pequeño test con **5 preguntas**.

Cada pregunta tendrá una respuesta correcta.

El programa debe:

1. Mostrar una pregunta.
2. Pedir la respuesta.
3. Comprobar si es correcta.
4. Llevar la puntuación.
5. Mostrar la puntuación final.

**Ejemplo:**

```text
¿Cuánto es 5 + 3?
8

¡Correcto!

...

Puntuación final: 4/5
```

---

# 📚 Recomendación

Se recomienda realizar los ejercicios siguiendo este orden:

```text
Nivel 1
   ↓
Variables y entrada de datos
   ↓
Nivel 2
   ↓
Condicionales
   ↓
Nivel 3
   ↓
Combinación de conceptos y resolución de problemas
```

Antes de programar, intenta siempre:

1. 📝 Entender el problema.
2. 🔍 Identificar los datos que necesitas.
3. 🧠 Pensar qué operaciones y condiciones necesitas.
4. ✏️ Escribir los pasos de la solución.
5. 💻 Programarlo.
6. 🧪 Probarlo con diferentes valores.
7. 🐛 Corregir los errores.

> 💡 **Consejo:** No intentes escribir todo el programa de golpe. Divide cada ejercicio en pequeños problemas y resuélvelos uno a uno.
