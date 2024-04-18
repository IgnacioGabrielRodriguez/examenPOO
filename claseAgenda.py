import fileinput
import eventos

class Agenda:

    def __init__(self):
        self.idEx = 0
        self.idTp = 0
        self.idRe = 0

    def agregarExamen(self,fecha,descripcion,materia):
        file = open("eventos.py","a")
        file.write(f"Ex{self.idEx} = Examenes('{fecha}', '{descripcion}', '{materia}')" + "\n")
        with open('ids.txt', 'a') as archivo:
            archivo.write("Ex" + str(self.idEx) + "\n")
        self.idEx += 1
        file.close()
    
    def agregarTrabajoPractico(self,fecha,descripcion,materia):
        file = open("eventos.py","a")
        file.write(f"Tp{self.idTp} = Examenes('{fecha}', '{descripcion}', '{materia}')" + "\n")
        with open('ids.txt', 'a') as archivo:
            archivo.write("Tp" + str(self.idTp) + "\n")
        self.idTp += 1
        file.close()
    
    def agregarReunionEstudio(self,fecha,descripcion):
        file = open("eventos.py","a")
        file.write(f"Re{self.idRe} = Examenes('{fecha}', '{descripcion}')" + "\n")
        with open('ids.txt', 'a') as archivo:
            archivo.write("Re" + str(self.idRe) + "\n")
        self.idRe += 1
        file.close()
    
    def visualizarEvento(self):
        for line in fileinput.input("ids.txt"):
            #for linea in fileinput.input("eventos.py"):
            #    if line in linea:
            #        objeto = getattr(eventos, line, None)
            #        if objeto is not None:
            #            print(objeto.str())
            #        else:
            #            print("No existe ningun objeto")
            print(line,end="")

            # Lo que queria hacer es que lea las ids linea por linea y si coincidian con el archivo de las varables, que se printee el metodo str
    
agendaEscolar = Agenda()
agendaEscolar.agregarExamen("21 de abril","w","Matematica")
agendaEscolar.agregarTrabajoPractico("20 de abril","X","Biologia")
agendaEscolar.visualizarEvento()

print("FIN DEL PROGRAMA")