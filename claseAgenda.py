import fileinput
import eventos

class Agenda:

    def __init__(self):
        self.id = 0

    def agregarExamen(self,fecha,descripcion,materia):
        file = open("eventos.py","a")
        file.write(f"Ex{self.id} = Examenes('{fecha}', '{descripcion}', '{materia}')" + "\n")
        eventos.agregarEvento(self.id)
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