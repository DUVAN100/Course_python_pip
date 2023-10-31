class Collatz:
    @classmethod
    def collatz(cls, num):
        if num % 2 == 0:
            result = num // 2
        else:
            result = 3 * num + 1
        return result

    @classmethod
    def start_process(cls):
        number = int(input("Ingresa un número entero: "))
        while number != 1:
            print(number)
            number = cls.collatz(number)
        return number

result = Collatz.start_process()
print("Resultado:", result)
