def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas = (total_segundos // 3600)
    print(horas)
    minutos = (horas % 60)
    print(minutos)
    segundos_rest = (total_segundos % 3600 % 60 )
    print(segundos_rest)
time()