import csv
import sys
from datetime import datetime

argumentos = sys.argv

data = {
    "csv": argumentos[1],
    "dni": argumentos[2],
    "salida": argumentos[3],
    "tipo": argumentos[4].upper(),
    "estado": True,
    "rangoFechas": argumentos[6] if len(argumentos) == 7 else True
}

if len(argumentos) >= 5:
    data["rangoFechas" if ":" in argumentos[5] else "estado"] = argumentos[5]




def estado(x):
     return x[-1] == data["estado"].upper() if (data["estado"] != True) else data["estado"]

def fechas(x):
    if data["rangoFechas"] != True:
        rango = data["rangoFechas"].split(":")
        fechaCSV = absoluteDate(int(x[-4]))
        return fechaCSV >= absoluteDate(rango[0]) and fechaCSV <= absoluteDate(rango[1])
    else:
        return True

def absoluteDate(date):
    if type(date) == str:
        date= datetime.timestamp(datetime.strptime(date, '%d-%m-%Y'))
    return int(date/(60*60*24))



file = open(data["csv"], "r", encoding='latin1')
lineas = list(csv.reader(file))

fild = [
    x for x in lineas
    if x[-3] == data["dni"] and x[-2] == data["tipo"] and estado(x) and fechas(x)  
]
file.close()

if data["salida"] == 'CSV':
    timeStampActual = str(datetime.now().timestamp())
    f = open("dni" + '-' + timeStampActual + '.csv',"a") 
    fileCSV=csv.writer(f)
    fileCSV.writerows(fild)
    f.close()
else:
    print(fild)

