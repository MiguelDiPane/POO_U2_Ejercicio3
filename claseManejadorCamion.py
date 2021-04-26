from claseCamion import Camion
import re

class ManejadorCamion:
    #Atributos
    __listaCamiones = []
    
    #Metodos
    def __init__(self):
        self.__listaCamiones = []
    
    def addCamion(self,id,nombre,patente,marca,tara):
        if id.isdigit() and tara.isdigit():
            id = int(id)
            tara = int(tara)
            if re.search(r'[\d\_\-\.+*]',nombre) != None: #busco numeros o simbolos en el nombre
                print('Error al ingresar el nombre. Este debe contener solo letras')
            elif re.search(r'[A-Z]{2}[\d]{3}[A-Z]{2}',patente) == None:
                print('Error al ingresar la patente, esta debe tener formato AA111AA')
            elif re.search(r'[\d\_\-\.+*]',marca) != None:
                print('Error al ingresar la marca. Este debe contener solo letras')
            elif id <= 0 or id > 20:
                print('El identificador debe ser de 1 a 20')
            else:
                newCamion = Camion(id,nombre,patente,marca,tara)
                self.__listaCamiones.append(newCamion)
        else:
            print('Error: identificador y tara deben ser un numero entero.')
    
    def getPesoCamion(self,id):
        if (type(id) == str and id.isdigit()) or (type(id) == int):
            return self.__listaCamiones[int(id)-1].getTara()
        else:
            return None

    
    def getPatentes(self):
        patentes = []
        for camion in self.__listaCamiones:
            patentes.append(camion.getPatente())
        return patentes
    
    def getConductores(self):
        conductores = []
        for camiones in self.__listaCamiones:
            conductores.append(camiones.getConductor())
        return conductores 
        
