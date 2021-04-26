class Camion:
    #Atributos
    __id = 0 #Numerico de 1 a 20
    __nombreConductor = ''
    __patente = ''
    __marca = ''
    __tara = 0 #Peso del camion vacio

    #Metodos
    def __init__(self,id=0,nombreCon='',patente='',marca='',tara=0):
        self.__id = id
        self.__nombreConductor = nombreCon
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara
     
    def getTara(self):
         return self.__tara
    def getPatente(self):
        return self.__patente
    def getConductor(self):
        return self.__nombreConductor