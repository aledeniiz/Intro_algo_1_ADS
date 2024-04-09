def calcular_area_triangulo(lado, altura):
    area = (lado * altura) / 2
    return area

# Ejemplo 1:
lado = float(input("Ingrese la medida de un lado del triángulo: "))
altura = float(input("Ingrese la altura relativa a este lado: "))
area = calcular_area_triangulo(lado, altura)
print("El área del triángulo es:", area)

"""2"""
"""Sí, este algoritmo también funciona para encontrar el área de un triángulo rectángulo. 
3Puedes usarlo proporcionando la medida de un lado como la base del triángulo y la medida del otro lado como la altura. 
Luego, puedes calcular el área de la misma manera que antes y obtendrás la cantidad de espacio dentro del triángulo rectángulo."""