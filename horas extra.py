def calcular_importe_horas_extra(salario_mensual_bruto, horas_extra):
    salario_semanal_bruto = salario_mensual_bruto / 4.33
    salario_diario_bruto = salario_semanal_bruto / 5
    tarifa_por_hora_normal = salario_diario_bruto / 7
    limite_horas_normales = 35 
    if horas_extra <= limite_horas_normales:
        importe_horas_extra = 0
    else:
        if 36 <= horas_extra <= 43:
            importe_horas_extra = (tarifa_por_hora_normal * 1.25) * (horas_extra - limite_horas_normales)
        elif horas_extra >= 44:
            importe_horas_extra = (tarifa_por_hora_normal * 1.5) * (horas_extra - limite_horas_normales)
    return importe_horas_extra

# Ejemplo 1:
salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
horas_extra_trabajadas_mes = int(input("Ingrese la cantidad de horas extra trabajadas al mes: "))
importe_horas_extra = calcular_importe_horas_extra(salario_mensual_bruto, horas_extra_trabajadas_mes)
print("El importe total de las horas extra que hay que pagar es:", importe_horas_extra)