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