
class Calculator:

    def sum(self, a: int, b: int) -> int:
        return a + b  

    def subtract(self, a: int, b: int) -> int: #De restar a substract
        return a - b  

    def multiply(self, a: int, b: int) -> int:
        return a * b  

    def divide(self, a: int, b: int) -> float:
        if b == 0:  #Condición de cero para evitar división por cero
            raise ValueError("No se puede dividir por cero")
        return a / b  
