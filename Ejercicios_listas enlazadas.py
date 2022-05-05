import time

class _Nodo:
    __slots__='_elemento', '_siguiente'

    def __init__(self, elemento,siguiente):
        self._elemento = elemento
        self._siguiente = siguiente
        

class ListaEnlazada:
    def __init__(self):
        self._frente = None
        self._final = None
        self._size = 0

    def __len__(self):
        return self._size

    def esta_vacio(self):
        return self._size == 0 #retorna un booleano hace una comparacion de lo que dice en el return

    def añadir_final(self, e):
        nuevo = _Nodo(e, None)
        if self.esta_vacio():
            self._frente = nuevo
        else:
            self._final._siguiente = nuevo
        self._final = nuevo
        self._size += 1

    def mostrar(self):
        p = self._frente
        while p:
            print(p._elemento,end=' --> ')#end, argumento que permite agregar texto al final de una cadena
            p = p._siguiente

    def buscar(self,key):
        p = self._frente
        index = 0
        while p:
            if p._elemento == key:
                return index
            p = p._siguiente
            index += 1
        return -1

    def añadir_inicio(self,e):
        nuevo = _Nodo(e, None)
        if self.esta_vacio():
            self._frente = nuevo
            self._final = nuevo
        else:
            nuevo._siguiente = self._frente
            self._frente = nuevo
        self._size += 1

    def añadir_posicion(self,e,posicion):
        nuevo = _Nodo(e,None)
        p = self._frente
        i = 1
        while i < posicion:
            p = p._siguiente
            i = i + 1
        nuevo._siguiente = p._siguiente
        p._siguiente = nuevo
        self._size += 1

    def eliminar_inicio(self):
        i = self._frente._elemento
        self._frente=self._frente._siguiente
        self._size -= 1
        return i

    def eliminar_final(self):
        p = self._frente
        while p:
            if p._siguiente == self._final:
                i = self._final._elemento
                p._siguiente = None
            p = p._siguiente
        self._size -= 1
        return i

    def eliminar_posicion(self,posicion):
        p = self._frente
        i = 1
        while i < posicion:
            p = p._siguiente
            i = i + 1
        e = p._siguiente._elemento
        p._siguiente = p._siguiente._siguiente
        self._size -= 1
        return e

L = ListaEnlazada()
tamano = 0
while tamano < 10:
    tamano = int(input("\nPor favor ingrese el número de datos que desea ingresar: "))


i=0
while i < tamano:
    L.añadir_final(int(input(f"\nPor favor ingrese el numero en la posición {i}\t")))
    L.mostrar()
    i += 1

i = 0
while i < tamano:
    print("\n\nElemento eliminado\t",L.eliminar_inicio())
    time.sleep(0.5)
    L.mostrar()
    time.sleep(0.5)
    i += 1
    if L._size == 0:
        print("La lista esta vacia\n")
