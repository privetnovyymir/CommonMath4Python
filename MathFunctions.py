class es_par_clase(object):
    def __init__(self, k, n):
        self.k = 2
        self.n = 12
        if n % k == 0:
            print(n, "es par")
        else:
            print(n, "es impar")

    def si_par(self):
        if self.n > 100 and self.n % 2 == 0:
            print("par of big numbers")
        else:
            print("par of little numbers")

    def max_divisor(n):
        maximo = 0
        i = 1
        while i < n:
            if n % i == 0:
                maximo = i
            i += 1
        return maximo

    print(max_divisor(12))

    # --------------------------------------------------#
    # calculo de un exponente positivo
    def potencia_positiva(base, exponente):
        if exponente == 0:
            return 1
        else:
            resultado = 1  # esto es una variable local ==> no existe fuera de la funcion
            while exponente > 0:
                resultado *= base
                exponente -= 1
            return resultado

    print(potencia_positiva(2, 3))

u = es_par_clase(2, 120)
u.n = 120 # importante marcar esto para que funione toda la estructura de 'class'
u.si_par()
