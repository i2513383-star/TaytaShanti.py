from capaDatos.dPersona import DPersona

class nPersona:
    def __init__(self):
        self.__dPersona = DPersona()
    
    def mostrarPersonas(self):
        return self.__dPersona.mostrarPersonas()
    
    def nuevaPersona(self, persona : dict):
        self.__dPersona.nuevaPersona(persona)
    
    def actualizasPersona(self, persona : dict , docIdentidad : str):
        return self.__dPersona.actualizarPersona(persona,docIdentidad)
    
    def eliminarPersona(self,docIdentidad:str):

        return self.__dPersona.eliminarPersona(docIdentidad)

from capaDatos.dProducto import DProducto

class nProducto:
    def __init__(self):
        self.__dProducto = DProducto()

    def mostrarProductos(self):
        return self.__dProducto.mostrarProductos()

    def nuevoProducto(self, producto: dict):
        self.__dProducto.nuevoProducto(producto)

    def actualizarProducto(self, producto: dict, id_producto: int):
        return self.__dProducto.actualizarProducto(producto, id_producto)

    def eliminarProducto(self, id_producto: int):
        return self.__dProducto.eliminarProducto(id_producto)
