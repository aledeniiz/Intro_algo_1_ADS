# Intro_algo_1_ADS
Alejandro Deniz Solana

Ejercicio 8: Porcentajes, IVA e inversiones
Para calcular el precio con todos los impuestos incluidos, primero necesitamos
saber el precio sin impuestos y el porcentaje de IVA. Luego, simplemente multiplicamos
el precio sin impuestos por el porcentaje de IVA, lo sumamos al precio sin impuestos y 
obtenemos el precio con todos los impuestos incluidos (TII).
Para calcular el importe de los intereses generados por un capital invertido, 
necesitamos conocer el capital invertido, la tasa de interés y el tiempo en meses. 
Simplemente multiplicamos el capital invertido por la tasa de interés (expresada como un decimal) y 
por el tiempo en meses para obtener el importe de los intereses generados.

Ejercicio 9: Media aritmética ponderada
Para calcular la media aritmética de tres números, simplemente sumamos los tres números y 
dividimos el resultado entre 3.
Para calcular la media ponderada cuando se dan los números y los coeficientes de ponderación,
multiplicamos cada número por su respectivo coeficiente de ponderación, sumamos los resultados
y dividimos entre la suma de los coeficientes de ponderación.

Ejercicio 10: Área del triángulo
Para calcular el área de un triángulo cuando se da la medida de un lado y la de la altura relativa
a este lado, simplemente multiplicamos la medida del lado por la altura y dividimos el resultado entre 2.
Sí, podemos utilizar el mismo algoritmo para calcular el área de un triángulo rectángulo si se dan 
las medidas de sus dos lados perpendiculares. Podemos considerar uno de los lados como la base del triángulo
y la longitud del otro lado como la altura relativa a este lado.

Ejercicio 11: Salario y horas extra
Dado un salario mensual bruto y la cantidad de horas extra trabajadas, necesitamos calcular 
el importe de las horas extra que hay que pagar. Para ello, primero calculamos la tarifa por 
hora normal a partir del salario mensual bruto, y luego aplicamos los aumentos correspondientes 
para las horas extra según las normas administrativas proporcionadas.

Ejercicio 12: Cuenta de depósito
Definimos el tipo de datos CUENTA, que incluye un atributo para el saldo de la 
cuenta y operaciones para depositar y retirar dinero.
Definimos las operaciones aplicables como depositar (para añadir dinero a la cuenta),
retirar (para sacar dinero de la cuenta) y obtener_saldo (para obtener el saldo actual de la cuenta).
Para permitir descubiertos en ciertas circunstancias, creamos una subclase 
llamada CuentaConDescubierto que hereda de la clase CUENTA. En esta subclase, 
modificamos la operación de retirar para permitir que el saldo sea negativo hasta cierto límite (descubierto autorizado).
