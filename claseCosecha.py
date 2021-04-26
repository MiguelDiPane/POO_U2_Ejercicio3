class Cosecha:
    #Atributos
    __listabid = [] #45 dias por 20 camiones
    
    #Metodos
    def __init__(self):
        #Inicializo lista
        self.__listabid = [[0 for i in range(20)] for j in range(45)]

    def mostrarTabla(self):
        print('#----------TABLA COSECHAS-----------#')
        for i in range(45):
            for j in range(20):
                print('{:7} '.format(self.__listabid[i][j]),end='')
            print()
        
    def registrarCarga(self,id,dia,pesoTotal,tara):
        if type(id) == str and type(dia) == str and id.isdigit() and dia.isdigit():
            id = int(id)
            dia = int(dia) 
        if type(id) == int and type(dia) == int and pesoTotal.isdigit() and tara != None:
            if id >= 1 and id <= 20:
                if dia >= 1 and dia <= 45:
                    pesoTotal = int(pesoTotal) #Considero entero por la precision de la bascula
                    pesoUva = pesoTotal - tara
                    self.__listabid[dia-1][id-1] += pesoUva
                else:
                    print('Error: El dia debe ser entre 1 y 45')
            else:
                print('Error: El camion ingresado no esta registrado, reintente.')
        else:
            print('Error: El identificador, el dia, el peso total y la tara deben ser enteros.')
 

    def showKilos(self,id): 
        if id.isdigit():
            id = int(id)
            cantTotal = 0
            if id >= 1 and id <= 20:
                for i in range(45):
                    cantTotal += self.__listabid[i][id-1]
                print('Cantidad total de kilos descargados: {}'.format(cantTotal))
            else:
                print('Error: El camion ingresado no esta registrado.')
        else:
            print('Error: El identificador debe ser un entero.')

    def getKilos(self,dia): 
        if dia.isdigit():
            dia = int(dia)
            if dia >= 1 and dia <= 45:
                return self.__listabid[dia-1][:]
            else:
                print('Error: El dia debe ser entre 1 y 45.')
                return None
        else:
            print('Error: El dia debe ser un entero.')
            return None