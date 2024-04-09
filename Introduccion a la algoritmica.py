"""Ejercicio 8"""
def calcular_TII(PSI, PIVA):
    impuesto = PSI * (PIVA / 100)
    TII = PSI + impuesto
    return TII

# Ejemplo 1:
precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
porcentaje_IVA = float(input("Ingrese el porcentaje de IVA: "))
precio_con_impuestos = calcular_TII(precio_sin_impuestos, porcentaje_IVA)
print("El precio con todos los impuestos incluidos es:", precio_con_impuestos)

"""2"""
def calcular_importe_intereses(C, I, T):
    IIG = C * (I / 100) * (T / 12)
    return IIG

# Ejemplo 2:
capital_invertido = float(input("Ingrese el capital invertido: "))
tasa_interes = float(input("Ingrese la tasa de interés (%): "))
tiempo_meses = int(input("Ingrese el tiempo en meses: "))
importe_intereses = calcular_importe_intereses(capital_invertido, tasa_interes, tiempo_meses)
print("El importe de los intereses generados es:", importe_intereses)