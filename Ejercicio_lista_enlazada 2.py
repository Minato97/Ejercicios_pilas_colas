import time

i = 0
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
        global i
        p = self._frente
        while p:
            if p._siguiente == self._final:
                i = self._final._elemento
                p._siguiente = None
            p = p._siguiente
        self._size -= 1
        print(i)

def movimiento(T1,T2,m):
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
    mostrar_todo()

def mostrar_todo():
    print("\nLista 1")
    L1.mostrar()
    print("\nLista 2")
    L2.mostrar()

def eliminacion_alterna(T1,T2,m):
    if T1._size == 1:
        print("\nSe ha eliminado el dato ",T1.eliminar_inicio())
    else:
        print("\nSe ha eliminado el dato ",T1.eliminar_final())
    if T2._size == 1:
        print("\nSe ha eliminado el dato ",T2.eliminar_inicio())
    else:
        print("\nSe ha eliminado el dato ",T2.eliminar_final())
    print("\n-------------------------------------------------------------------------------------")
    print("\nMovimiento de eliminacion ", m)
    mostrar_todo()




L1 = ListaEnlazada()
L2 = ListaEnlazada()

tamano = int(input("\nPor favor ingrese el número de datos que desea ingresar: "))

j = 0
while j < tamano:
    L1.añadir_final(int(input(f"\nPor favor ingrese el numero en la posición {j}\t")))
    L1.mostrar()
    j += 1


movimiento(L2,L1,1)
movimiento(L2,L1,2)
movimiento(L2,L1,3)

eliminacion_alterna(L1,L2,1)
eliminacion_alterna(L1,L2,2)
eliminacion_alterna(L1,L2,3)


