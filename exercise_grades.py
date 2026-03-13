def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio = ((nota2 + nota3 + nota1)/3)
    print(promedio)
    mayor_nota = max(nota2 , nota3 , nota1)
    print(mayor_nota)
    menor_nota = min(nota2 , nota3 , nota1)
    print(menor_nota)
    puntos = (10 - promedio)
    print(puntos)
grades()