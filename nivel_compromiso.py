# nombre: Daniel Mauricio Zamorano Rialpe
# Grupo: 213022-545
# Programa: Ingenieria en Electronica
# Codigo fuente: Autoria propia

# cliente[ID, Duracion(segundos), numero de clics]
cliente=[
    [100,180,10],
    [200,59,6],
    [300,150,5],
    [400,190,11],
    [500,200,9]
]

def compromiso(cliente):
    for i in range(len(cliente)):
        if cliente[i][1] > 180 and cliente[i][2] > 8:
            print("El cliente con id", cliente[i][0], "tiene un compromiso alto")
        elif cliente[i][1] < 60 or cliente[i][2] < 3:
            print("El cliente con id", cliente[i][0], "tiene un compromiso bajo")
        else:
            print("El cliente con id", cliente[i][0], "tiene un compromiso medio")

compromiso(cliente)
