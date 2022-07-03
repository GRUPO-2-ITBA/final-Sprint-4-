import csv
import sys
from datetime import datetime

t1 = str(int(datetime.now().timestamp()))

argumentos = sys.argv

def estado(x):
    return  x[-1] == data["estado"].upper() if data["estado"] != None else True


data = {
    "csv": argumentos[1],
    "dni": argumentos[2],
    "salida": argumentos[3],
    "tipo": argumentos[4].upper(),
    "estado": None,
    "rangoFechas": argumentos[6] if len(argumentos) == 7 else None
}

if len(argumentos) > 5:
    data["rangoFechas" if ":" in argumentos[5] else "estado"] = argumentos[5]
    
file = open(data["csv"], "r", encoding='latin1')
lineas = csv.reader(file)
filtrado = [
    x for x in lineas
    if x[-3] == data["dni"] and x[-2] == data["tipo"] and estado(x)
]
file.close()

if "salida "== 'CSV':
    timeStampActual = str(datetime.now().timestamp())
    f = open("dni" + '-' + timeStampActual + '.csv',"a") 
    fileCSV=csv.writer(f)
    fileCSV.writerows(filtrado)
    f.close()
 print(filtrado)

