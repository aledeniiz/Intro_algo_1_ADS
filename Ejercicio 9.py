"""9"""
def calcular_media_aritmetica(A, B, C):
    suma = A + B + C
    media_aritmetica = suma / 3
    return media_aritmetica

# Ejemplo 1:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
media = calcular_media_aritmetica(num1, num2, num3)
print("La media aritmética de los tres números es:", media)

"""2"""
def calcular_media_ponderada(A, B, C, P_A, P_B, P_C):
    suma_ponderada = A * P_A + B * P_B + C * P_C
    suma_coeficientes = P_A + P_B + P_C
    media_ponderada = suma_ponderada / suma_coeficientes
    return media_ponderada

# Ejemplo 2:
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
coef1 = float(input("Ingrese el coeficiente de ponderación para el primer número: "))
coef2 = float(input("Ingrese el coeficiente de ponderación para el segundo número: "))
coef3 = float(input("Ingrese el coeficiente de ponderación para el tercer número: "))
media_ponderada = calcular_media_ponderada(num1, num2, num3, coef1, coef2, coef3)
print("La media ponderada de los tres números es:", media_ponderada)