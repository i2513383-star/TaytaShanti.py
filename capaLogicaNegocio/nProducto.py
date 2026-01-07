from capaDatos.dProducto import DProducto

class nProducto:
    def __init__(self):
        self.__dProducto = DProducto()

    def mostrarProductos(self):
        return self.__dProducto.mostrarProductos()

    def nuevoProducto(self, producto: dict):
        return self.__dProducto.nuevoProducto(producto)

    def actualizarProducto(self, producto: dict, id: int):
        return self.__dProducto.actualizarProducto(producto, id)

    def eliminarProducto(self, id: int):
        return self.__dProducto.eliminarProducto(id)
