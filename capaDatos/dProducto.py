from conexion import conexionDB

class DProducto:
    def __init__(self):
        self.__db = conexionDB().conexionSupabase()
        self.__nombreTabla = "productos"

    def ejecutarConsultas(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
                return resultado
            else:
                return consulta.execute()
        except Exception as e:
            raise e

    def mostrarProductos(self):
        consulta = self.__db.table(self.__nombreTabla).select('*')
        return self.ejecutarConsultas(consulta, 'SELECT')

    def nuevoProducto(self, producto: dict):
        consulta = self.__db.table(self.__nombreTabla).insert(producto)
        return self.ejecutarConsultas(consulta)

    def actualizarProducto(self, producto: dict, id: int):
        consulta = (
            self.__db
            .table(self.__nombreTabla)
            .update(producto)
            .eq('id', id)
        )
        return self.ejecutarConsultas(consulta)

    def eliminarProducto(self, id: int):
        consulta = (
            self.__db
            .table(self.__nombreTabla)
            .delete()
            .eq('id', id)
        )
        return self.ejecutarConsultas(consulta)
