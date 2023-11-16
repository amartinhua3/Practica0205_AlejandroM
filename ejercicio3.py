def area_circ(r):
    import math
    
    '''Función que calcula el área de un circulo
Parámetros:
    import math: Importa un valor matematico dentro de la función
    r: Distancia del radio de una circunferencia
    math pi: establece el valor de pi
Salida:
    Un numero real con el área del circulo de 𝛑 y radio especificados  '''

    return math.pi * (r)**2
area_circ(2)

def vol_cilin(r, h):
    '''Función que calcula el volumen de un cilindro a partir de la función del area del circulo
#Parámetros: 
    h: Representa la altura del cilindro
#Salida: Un número calculado que es el volumen del cilindro'''
    print(area_circ(r) * h)
    return  
vol_cilin(2, 7)