class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular    
        self.__saldo = saldo        

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Error: No se pueden hacer depósitos negativos.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: No se pueden hacer retiros negativos.")
        elif cantidad > self.__saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")

    def consultar_saldo(self):
        return self.__saldo

    def consultar_titular(self):
        return self.__titular



cuenta = CuentaBancaria("Asael", 7000)

print("Titular:", cuenta.consultar_titular())
print("Saldo inicial:", cuenta.consultar_saldo())

cuenta.depositar(560)   
cuenta.depositar(-255)  

cuenta.retirar(300)     
cuenta.retirar(400)    
cuenta.retirar(-125)     

print("Saldo final:", cuenta.consultar_saldo())
