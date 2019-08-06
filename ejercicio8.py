class Empleado:
    def __init__(self):
        self.nombre=""
        self.apellidos=""
        self.edad=19
        
    def saludar(self):
        return "Hola me llamo ", self.nombre
    
    def saludar2(self):
    print ("hola me llamo", self.nombre+ , "el saludar 2")
s

emp = Empleado()
emp.nombre="eduardo mendoza"
print (emp.saludar())

