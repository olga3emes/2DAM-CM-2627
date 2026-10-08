#ESTRUCTURAS DE DATOS
#====================
#COLECCIONES
from collections import deque, Counter, namedtuple
# deque: cola doble
cola = deque(["a", "b", "c"])
cola.append("d")
cola.appendleft("z")
print("Deque:", cola)
# Counter: contar elementos
letras = Counter("abracadabra")
print("Contador:", letras)
# namedtuple: tupla con nombre
Punto = namedtuple("Punto", "x y")
p = Punto(3, 4)
print("Punto:", p.x, p.y)

#COLAS DE PRIORIDAD
import heapq
numeros = [5, 3, 8, 1]
heapq.heapify(numeros)
print("Min-heap:", numeros)
# Insertar nuevo elemento
heapq.heappush(numeros, 2)
print("Heap con nuevo elemento:", numeros)
# Extraer el menor
menor = heapq.heappop(numeros)
print("Elemento más pequeño:", menor)

#ARRAYS - VECTORES
import array
# Crear un array de enteros
a = array.array('i', [1, 2, 3, 4])
a.append(5)
print("Array de enteros:", a.tolist())

#COLAS - SEGURAS PARA HILOS
from queue import Queue, LifoQueue
# FIFO Queue
cola = Queue()
cola.put("uno")
cola.put("dos")
print("FIFO:", cola.get(), cola.get())
# LIFO Queue (pila)
pila = LifoQueue()
pila.put("uno")
pila.put("dos")
print("LIFO:", pila.get(), pila.get())
