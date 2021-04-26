import csv
import time
from claseManejadorCamion import ManejadorCamion
from claseCosecha import Cosecha
from claseMenu import Menu

def test():
    print("Test de creacion de camiones")
    manejadorTest = ManejadorCamion()
    nomAr = 'camionesTest.csv'
    archivo = open(nomAr)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            time.sleep(0.5)
            print('Datos: {}'.format(fila))
            manejadorTest.addCamion(fila[0],fila[1],fila[2],fila[3],fila[4])
    archivo.close()
    print('Test finalizado, presione ENTER para continuar...')
    print('Test de carga de cosechas erroneas')
    cosechaTest = Cosecha()
    nomAr = 'tablaCosechaTest.csv'
    print('Lectura de archivo: {}'.format(nomAr))
    archivo = open(nomAr)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    pesosTotales = []
    for fila in reader:
        if bandera:
            bandera = False
        else:
            pesosTotales.append(fila)
    archivo.close() 
            
    #Cargo cosecha
    cosechaTest = Cosecha()
    for dia in range(45):
        for id in range(20):
            tara = manejadorCamion.getPesoCamion(id+1)
            cosechaTest.registrarCarga(id+1,dia+1,pesosTotales[dia][id],tara)                  
    print('Carga finalizada.')
    
if __name__ == '__main__':
    miCosecha = Cosecha()
    manejadorCamion = ManejadorCamion()

    #Cargo camiones en lista de camiones 
    nomAr = 'camiones.csv'
    archivo = open(nomAr)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            manejadorCamion.addCamion(fila[0],fila[1],fila[2],fila[3],fila[4])
    archivo.close()

    menuPrincipal = Menu()
    menuPrincipal.define_menu(['[1]- Leer cosecha de archivo','[2]- Actividad 3','[3]- Carga manual de cosecha','[4]- Mostrar tabla cosecha','[5]- Ejecutar funcion test','[0]- Salir'])
    menuPrincipal.showMenu()
    op = menuPrincipal.selectOption()
    while op != 0:
        if op == 1:
            #Cargo archivo cosecha
            nomAr = 'tablaCosecha.csv'
            print('Lectura de archivo: {}'.format(nomAr))
            archivo = open(nomAr)
            reader = csv.reader(archivo,delimiter=',')
            bandera = True
            pesosTotales = []
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    pesosTotales.append(fila)
            archivo.close() 
            
            #Cargo cosecha
            for dia in range(45):
                for id in range(20):
                    tara = manejadorCamion.getPesoCamion(id+1)
                    miCosecha.registrarCarga(id+1,dia+1,pesosTotales[dia][id],tara)
                    
            print('Carga finalizada.')
            input('Presione ENTER para continuar...')

        elif op == 2:
            menuSecundario = Menu()
            menuSecundario.define_menu(['[1]- Mostrar total kilos descargados de un camion','[2]- Listado segun dia','[0]- Volver al menu principal'])
            menuSecundario.showMenu()
            op2 = menuSecundario.selectOption()
            while op2 != 0:
                if op2 == 1:
                    id = input('Ingrese identificador de camion: ')
                    kilos = miCosecha.showKilos(id)
                    input('Presione ENTER para continuar...')
                elif op2 == 2:
                    dia = input('Ingrese un dia: ') 
                    kilosDiarios = miCosecha.getKilos(dia) 
                    if kilosDiarios != None:
                        patentes = manejadorCamion.getPatentes()
                        conductores = manejadorCamion.getConductores()
                        tabla = [patentes,conductores,kilosDiarios]
                        print('{:15}{:30}{:15}'.format('PATENTE','CONDUCTOR','CANTIDAD DE KILOS'))
                        for i in range(len(patentes)):
                            print('{:15}{:22}{:15}'.format(patentes[i],conductores[i],kilosDiarios[i]))
                    input('Presione ENTER para continuar...')  
                menuSecundario.showMenu()
                op2 = menuSecundario.selectOption()

        #Asignacion manual de cosechas
        elif op == 3:
            id = input('Ingrese identificador camion (0 para terminar): ')
            while id != '0':
                dia = input('Ingrese dia: ')
                pesoTotal = input('Ingrese peso: ')
                tara = manejadorCamion.getPesoCamion(id)
                miCosecha.registrarCarga(id,dia,pesoTotal,tara) 
                id = input('Ingrese identificador camion (0 para terminar): ')       
          
        elif op == 4:
            miCosecha.mostrarTabla()
            input('Presione ENTER para continuar...')
        #Funcion test
        elif op == 5:
            test()
            input('Presione ENTER para volver al menu...')
      
        menuPrincipal.showMenu()
        op = menuPrincipal.selectOption()