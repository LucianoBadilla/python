import math

def calcular_circunferencia(radio):
    # Redondeamos el valor de pi a 6 decimales
    pi = round(math.pi, 6)
    # Calculamos la circunferencia utilizando la fórmula: 2 * pi * radio
    circunferencia = 2 * pi * radio
    return circunferencia

def main():
    # Definimos una lista de radios para los que queremos calcular la circunferencia
    radios = [3, 8, 10]

    # Iteramos sobre cada radio en la lista
    for radio in radios:
        # Calculamos la circunferencia para el radio actual
        circunferencia = calcular_circunferencia(radio)
        # Imprimimos un mensaje que muestra el radio y la circunferencia calculada
        print(f"Para un radio de {radio}, la circunferencia es: {circunferencia}")

if __name__ == "__main__":
    # Llamamos a la función main() para iniciar el programa
    main()
