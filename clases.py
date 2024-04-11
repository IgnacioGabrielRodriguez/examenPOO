class Eventos:

    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

class Examenes(Eventos):

    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia

    def __str__(self) -> str:
        return f"Examen de {self.materia}. {self.descripcion}. Fecha: {self.fecha}"

class TrabajosPracticos(Eventos):

    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia
    
    def __str__(self) -> str:
        return f"Trabajo practico de {self.materia}. {self.descripcion}. Fecha: {self.fecha}"

class ReunionDeEstudio(Eventos):

    def __init__(self, fecha, descripcion):
        super().__init__(fecha, descripcion)
    
    def __str__(self) -> str:
        return f"Reunion de estudio: {self.descripcion}. Fecha: {self.fecha}"

class Agenda:

    def __init__(self):
        pass
    
    