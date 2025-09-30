class Calculo_Numerico:
    def __init__(self, numero: int):
        self.numero = numero

    def calculo_factorial(self) -> int:
        """
        Este método permite calcular el factorial de un número.
        """
        resultado_fact = 1
        
        if self.numero == 0:
            return 1
        
        mi_numero = self.numero
        while mi_numero >= 1:
            resultado_fact = resultado_fact * mi_numero
            mi_numero = mi_numero - 1
        return resultado_fact

    def lista_divisores(self) -> list:
        """
        Este método permite encontrar la lista de divisores de un número
        """
        resultados_divisores = []
        for divisor in range(1, self.numero + 1):
            if self.numero % divisor == 0:
                resultados_divisores.append(divisor)
                
        return resultados_divisores

    def esPrimo(self):
        """
        Este método permite verificar si un número es primo
        """
        lista_dos_divisores = self.lista_divisores()
        if len(lista_dos_divisores) == 2:
            print("El número", self.numero, "es primo")
        else:
            print("El número", self.numero, "no es primo")

    def esPar(self):
        """
        Este método permite verificar si un número es par
        """
        if self.numero % 2 == 0:
            print("El número", self.numero, "es Par")
        else:
            print("El número", self.numero, "es Impar")


primer_calculo = Calculo_Numerico(5)

factorial_5 = primer_calculo.calculo_factorial()
divisores_5 = primer_calculo.lista_divisores()
print("El factorial del número 5 es:", factorial_5)
print("La lista de divisores del número 5 es:", divisores_5)
primer_calculo.esPar()
primer_calculo.esPrimo()
print()

segundo_calculo = Calculo_Numerico(14)

factorial_14 = segundo_calculo.calculo_factorial()
divisores_14 = segundo_calculo.lista_divisores()
print("El factorial del número 14 es:", factorial_14)
print("La lista de divisores del número 14 es:", divisores_14)
segundo_calculo.esPar()
segundo_calculo.esPrimo()