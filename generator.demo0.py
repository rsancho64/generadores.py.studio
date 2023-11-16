#! /usr/bin/python3
#  GENERADORES
# return vs yield como respuestas de las *FUNCIONES (constructoras)* vs *los GENERADORES*
# return: retorno final y definitivo del control, y de la estructura de datos respondida.
#
#  yield: retorno de un *next* item retornable, hasta agotamiento. 
#       Puede generar una excepcion StopIteration
# 

def paresWReturn(howmany):
    """un constructor retorna construcciones"""
    answ = []
    for i in range(howmany):
        if i % 2 == 0:
            answ.append(i)
    return answ

def paresWYield(howmany):
    """un generador es un "flujo agotable". 
    Ofrece en cada "llamada asincrona" un item"""
    for i in range(howmany):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":

    print(paresWReturn(20))  # imprime construccion retornada, completa
    print(paresWYield(20))   # imprime <generator obj ..> (No se usa como objeto)

    g = paresWYield(20)  # generador
    for it in g:
        print(it, end=", ")
    print()

    # aserto: g agotado.
    # print(next(g))          # lanza la excepcion StopIteration
    # print("no se alcanza")

    print("se alcanza")

    for it in g:  # g sigue 
        print(it) # no se alcanza

    g = paresWYield(20)  # generador regenerado

    print(next(g))
    print(next(g))
    print(next(g))

    # el generador 'generador' esta algo consumido, no del todo... 


