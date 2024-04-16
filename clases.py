import fileinput
import eventos

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
        return f"Trabajo practico de {self.materia}. {self.descripcion}. Fecha de entrega: {self.fecha}"

class ReunionDeEstudio(Eventos):

    def __init__(self, fecha, descripcion):
        super().__init__(fecha, descripcion)
    
    def __str__(self) -> str:
        return f"Reunion de estudio: {self.descripcion}. Fecha: {self.fecha}"

class Agenda:

    def __init__(self):
        self.id = 0

    def agregarExamen(self,fecha,descripcion,materia):
        file = open("eventos.py","a")
        file.write(f"Ex{self.id} = Examenes('{fecha}', '{descripcion}', '{materia}')" + "\n")
        eventos.events.append(self.id)
        self.id += 1
        file.close()
    
    def visualizarEvento(self):
        for line in fileinput.input("eventos.py"):
            print(line,end="")
    
agendaEscolar = Agenda()
agendaEscolar.agregarExamen("21 de abril","w","Matematica")
agendaEscolar.agregarExamen("21 de abril","w","Matematica")
agendaEscolar.visualizarEvento()

print("FIN DEL PROGRAMA")