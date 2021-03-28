"""
# jika menggunakan class
class functionOperation():
    
    def __init__(self, start:int = 2, stop:int = 10, operation:str = "plus1"):
        self.start = start
        self.stop = stop
        self.operation = operation
    
    def function(self):
        if (self.operation == 'plus1'):
            range_start = self.start
            range_stop = self.stop + 1
            plus_satu = [hasil for hasil in range(range_start, range_stop)]
            return plus_satu

        elif (self.operation == 'fibonacci'):
            def fib(n):
                param = 5 ** 0.5 / 2 + 0.5
                return round((param ** n - (1 - param) ** n) / 5 ** 0.5)   
            fibonacci = []
            range_start = 0
            range_stop = self.stop + 1
            for n in range(range_start, range_stop):
                if (fib(n) > self.stop):
                    break
                elif (fib(n) >= self.start):
                    fibonacci.append(fib(n))
            return fibonacci
        
        elif (self.operation == 'kuadrat'):
            hasil = 0
            kuadrat = []
            range_start = 1
            range_stop = self.stop + 1
            for pangkat in range(range_start, range_stop):
                hasil = self.start**pangkat
                if (hasil > self.stop):
                    break
                kuadrat.append(hasil)
            return kuadrat
        
        else:
            return "Operasi yang dilakukan hanya 'plus1', 'fibonacci', dan 'kuadrat'"
"""

def function(start:int, stop:int, operation:str):
    if (operation == 'plus1'):
        range_stop = stop + 1
        plus_satu = [hasil for hasil in range(start, range_stop)]
        return plus_satu

    elif (operation == 'fibonacci'):
        def fib(n):
            param = 5 ** 0.5 / 2 + 0.5
            return round((param ** n - (1 - param) ** n) / 5 ** 0.5)   
        fibonacci = []
        range_start = 0
        range_stop = stop + 1
        for n in range(range_start, range_stop):
            if (fib(n) > stop):
                break
            elif (fib(n) >= start):
                fibonacci.append(fib(n))
        return fibonacci
    
    elif (operation == 'kuadrat'):
        hasil = 0
        kuadrat = []
        range_start = 1
        range_stop = stop + 1
        for iterasi in range(range_start, range_stop):
            hasil = start**iterasi
            if (hasil > stop):
                break
            kuadrat.append(hasil)
        return kuadrat
    
    else:
        return "Operasi yang dilakukan hanya 'plus1', 'fibonacci', dan 'kuadrat'"
