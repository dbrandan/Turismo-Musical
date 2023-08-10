import json
class Usuario:
    def __init__(self,id: str, nombre: str, apellido: str, historial_de_eventos: list[int], clave: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_de_eventos = historial_de_eventos
        self.clave = clave

    def to_json(self):
        return {"id": self.id,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "historial_de_eventos": self.historial_de_eventos,
                "clave" : self.clave
        
        } 
    
        
    @classmethod
    def from_json(cls, json_data) :
        data = json.loads(json_data)
        # carga de json
        id = data ["id"]
        nombre = data ["nombre"]
        apellido = data ["apellido"]
        historial_de_eventos = data ["historial_de_eventos"]
        clave= data["clave"]
        
        return cls(id, nombre, apellido, historial_de_eventos,clave)

    

        