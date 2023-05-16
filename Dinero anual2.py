class ingreso: 
    def __init__(self,anual,anio):
        self.anual = anual
        self.año = anio 
        self.libros = 0
        self.bus = 0
        self.cine = 0
        self.madres = 0
        
        
    def caldistribucion(self):
        self.libros = int(self.anual*0.5)
        self.bus =  int((self.anual*0.2) / 2)
        self.cine = int((self.anual*0.2)/ 5)
        self.madres = int(self.anual*0.1)
        self.año = int(self.año*self.anual)
        
    def mostrar(self):
        print("Cantidad destinada a libros y utiles: $","{:,}".format(self.libros))
        print("Entradas de bus posibles: $","{:,}".format(self.bus))
        print("Entradas de cine posibles: $","{:,}".format(self.cine))
        print("Cantidad destinada a regalo de madres: $","{:,}".format(self.madres))
        
        
    def carrera(self):
        print("El total de dinero en la carrera es de: ","{:,}".format(self.año))
        
        
cantidad = int(input("Ingrese la cantidad de dinero anual: "))
carrera = int(input("Cantidad de años de la carrera: "))

dinero = ingreso(cantidad,carrera)

dinero.caldistribucion()

dinero.mostrar()

dinero.carrera()




