class ingreso: 
    def __init__(self,anual):
        self.anual = anual
        self.libros = 0
        self.bus = 0
        self.cine = 0
        self.madres = 0
        
    def caldistribucion(self):
        self.libros = int(self.anual*0.5)
        self.bus =  int((self.anual*0.2) / 2)
        self.cine = int((self.anual*0.2)/ 5)
        self.madres = int(self.anual*0.1)
        
    def mostrar(self):
        print("\nCantidad destinada a libros y utiles: $","{:,}".format(self.libros))
        print("Entradas de bus posibles: $","{:,}".format(self.bus))
        print("Entradas de cine posibles: $","{:,}".format(self.cine))
        print("Cantidad destinada a regalo de madres: $","{:,}".format(self.madres))
        
    def cambiar(self):
        self.libros = int(self.anual*0.5)
        self.bus =  int((self.anual*0.2) / pb)
        self.cine = int((self.anual*0.2)/ pc)
        self.madres = int(self.anual*0.1)
        
cantidad = int(input("Ingrese la cantidad de dinero anual: "))

dinero = ingreso(cantidad)

dinero.caldistribucion()

dinero.mostrar()

rep=1
while rep==1:
    rep=int(input("\n\nDesea cambiar los valores del bus y cine? (1= si, 2= no)"))
    if rep==1: 
        pb=int(input("\nIngrese el valor de un pasaje de bus: "))
        pc=int(input("\nIngrese el valor de una entrada de cine: "))
        
        dinero.cambiar()
        dinero.mostrar()
        
                
    else: break
    
    
    





