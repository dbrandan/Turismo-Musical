import json
class Ruta_Visita:
    def __init__(self, id: int, nombre: str, destinos: list[str]):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        return {"id": self.id,
                "nombre": self.nombre,
                "destinos": self.destinos,
                } 
        
    @classmethod
    def from_json (cls, json_data) :
        data = json.loads(json_data)
        # carga de json
        id = data ["id"]
        nombre = data ["nombre"]
        destinos = data ["destinos"]
        
        return cls(id, nombre, destinos)
    
