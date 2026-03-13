def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    prom = ((num1 + num3 +num4 + num2)/4)
    print(prom)
    mayor = max(num1 , num4 , num2 , num3)
    print(mayor)
    menor = min(num1 , num4 , num2 , num3)
    print(menor)
    rango = (mayor - menor)
    print (rango)
statistics()