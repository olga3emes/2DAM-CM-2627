#ITERADORES
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Uso del iterador
data = [1, 2, 3, 4, 5]
iterator = MyIterator(data)
for item in iterator:
    print(item)

# Generador
def my_generator(data):
    for item in data:
        yield item
# Uso del generador
gen = my_generator(data)
for item in gen:
    print(item)
# Comprensión de generadores
gen_comp = (x * x for x in range(5))
for item in gen_comp:
    print(item)
# Iteradores y generadores con funciones integradas
def square(x):
    return x * x
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
# Uso de la función integrada map
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
for num in squared_numbers:
    print(num)
