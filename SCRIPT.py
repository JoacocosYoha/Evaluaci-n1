import time
import os
os.system('cls')
print("/////////////////////////////////////////")
print("Bienvenido al verificador de conectividad")
print("/////////////////////////////////////////")
finalizado=False
while True:
    while finalizado==False:
        ip=(input("Ingrese la direccion IP que desea revisar: "))
        time.sleep(1)
        url=(input("Ingrese el URL que desea verificar. formato:(www.paginaweb.cl): "))
        time.sleep(0.5)
        os.system('cls')
        print("espere ahora los resultados...")
        os.system('ping -c 3 '+ ip +' >> pingip.txt')
        time.sleep(1)
        os.system('ping -c 3 '+url +'>> pingurl.txt')
        time.sleep(0.5)
        os.system('cls')
        print("muchas gracias...")
        print("Estos son los resultados para la ip")
        os.system('cat pingip.txt | grep received')
        time.sleep(0.5)
        print("Y para la url este es el resultado: ")
        os.system('cat pingurl.txt | grep received')
        time.sleep(0.5)
        break
    break
