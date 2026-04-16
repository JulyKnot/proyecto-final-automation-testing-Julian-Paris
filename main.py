def Sumar(a, b):
    return a + b

def Restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b

if __name__ == "__main__":
    try:
        print("Calculadora Lineal")
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        op = input("Ingrese la operación (+, -, *, /): ")

        if op == '+':
            resultado = Sumar(a, b)
        elif op == '-':
            resultado = Restar(a, b)
        elif op == '*':
            resultado = Multiplicar(a, b)
        elif op == '/':
            resultado = Dividir(a, b)
        else:
            resultado = "Operación no válida"

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Entrada inválida. Por favor ingrese números válidos.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")