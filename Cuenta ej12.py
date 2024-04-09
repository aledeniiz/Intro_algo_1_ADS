class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
            return True
        else:
            return False

    def obtener_saldo(self):
        return self.saldo
    
"""Las operaciones aplicables son:
depositar(cantidad): Permite depositar una cantidad en la cuenta.
retirar(cantidad): Permite retirar una cantidad de la cuenta, siempre y cuando el saldo resultante no sea negativo.
obtener_saldo(): Devuelve el saldo actual de la cuenta."""

class CuentaConDescubierto(Cuenta):
    def __init__(self, saldo, descubierto_autorizado):
        super().__init__(saldo)
        self.descubierto_autorizado = descubierto_autorizado

    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.descubierto_autorizado:
            self.saldo -= cantidad
            return True
        else:
            return False