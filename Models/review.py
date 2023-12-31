import json

class Review:
    def __init__( self, id: int ,id_evento: int ,id_usuario: int ,calificacion: int ,comentario: str ,animo: bool):
        """ 
        calificacion 1-5
        animo bolean
        """
        
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_json(self):
        return {"id": self.id,
                "id_evento": self.id_evento,
                "id_usuario": self.id_usuario,
                "calificacion": self.calificacion,
                "comentario": self.comentario,
                "animo": self.animo
        } 
        
    @classmethod
    def from_json (cls, json_data) :
        data = json.loads(json_data)
        # carga de json
        id = data ["id"]
        id_evento = data ["id_evento"]
        id_usuario = data ["id_usuario"]
        calificacion = data ["calificacion"]
        comentario = data ["comentario"]
        animo = data ["animo"]
        return cls(id, id_evento, id_usuario, calificacion, comentario, animo)
 