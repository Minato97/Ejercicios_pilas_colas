import time

m = 1
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
            print(p._elemento,end=' --> ')
            #time.sleep(0.25)#end, argumento que permite agregar texto al final de una cadena
            p = p._siguiente


    def añadir_inicio(self,e):
        nuevo = _Nodo(e, None)
        if self.esta_vacio():
            self._frente = nuevo
            self._final = nuevo
        else:
            nuevo._siguiente = self._frente
            self._frente = nuevo
        self._size += 1

    def eliminar_inicio(self):
        i = self._frente._elemento
        self._frente=self._frente._siguiente
        self._size -= 1
        return i




    def eliminar_final(self):
        i = self._final._elemento
        if self.esta_vacio():
            print("La lista esta vacio")
            return
        p = self._frente
        while p:
            if p._siguiente == self._final:
                i = self._final._elemento
                p._siguiente = None
            p = p._siguiente
        self._size -= 1
        return i

    def eliminar_ultimo(self):
        if self.esta_vacio():
            print('Lista vacia')
            return
        p = self._frente
        i = 1
        while i < len(self) - 1:
            p = p._siguiente
            i = i + 1
        self._final = p
        p = p._siguiente
        e = p._elemento
        self._final._siguiente = None
        self._size -= 1
        return e

def eliminar_alternado(T1,T2):
    i = 0
    while i < tamano // 2:
        print("\n\nLista 1")
        if T1._size == 1:
            print("\nElemento eliminado\t", T1.eliminar_inicio())
            print("\nLa lista esta vacia")
        else:
            print("\nElemento eliminado\t", T1.eliminar_ultimo())
        time.sleep(0.5)
        T1.mostrar()
        time.sleep(0.5)

        print("\n\nLista 2")
        if T2._size == 1:
            print("\nElemento eliminado\t", T2.eliminar_inicio())
            print("\nLa lista esta vacia")
        else:
            print("\nElemento eliminado\t", T2.eliminar_ultimo())
        time.sleep(0.5)
        T2.mostrar()
        time.sleep(0.5)
        i += 1


def movimiento(T1,T2):
    global m
    T1.añadir_final(T2._final._elemento)
    if T2._size == 1:
        T2.eliminar_inicio()
    else:
        T2.eliminar_final()
    p = T2._frente
    while p:
        if p._siguiente == None:
            T2._final = p
        p = p._siguiente
    print("\n-------------------------------------------------------------------------------------")
    print("\nMovimiento ", m)
    m +=1
    mostrar_todo()

def mostrar_todo():
    print("\nLista 1")
    L1.mostrar()
    print("\nLista 2")
    L2.mostrar()

def num_mov():
    j = 0
    while j < tamano//2:
        movimiento(L2,L1)
        j += 1




L1 = ListaEnlazada()
L2 = ListaEnlazada()

tamano = int(input("\nPor favor ingrese el número de datos que desea ingresar: "))

j = 0
while j < tamano:
    L1.añadir_final(int(input(f"\nPor favor ingrese el numero en la posición {j}\t")))
    L1.mostrar()
    j += 1


num_mov()

while L1._size != 0 and L2._size != 0:
    eliminar_alternado(L1,L2)


