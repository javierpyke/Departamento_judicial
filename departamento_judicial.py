

class Dep_judicial():
    def __init__(self,numero,fuero,nombre,tipo_de_ente,direccion,localidad,departamento_judicial,telefono,latitud,longitud):
        self.__numero = numero
        self.__fuero = fuero
        self.__nombre = nombre
        self.__tipo_de_ente = tipo_de_ente
        self.__direccion = direccion
        self.__localidad = localidad
        self.__departamento_judicial = departamento_judicial
        self.__telefono = telefono
        self.__latitud = latitud
        self.__longitud = longitud

    def get_numero(self):
        return self.__numero

    def get_fuero(self):
        return self.__fuero

    def get_nombre(self):
        return self.__nombre

    def get_tipo_de_ente(self):
        return self.__tipo_de_ente

    def get_direccion(self):
        return self.__direccion

    def get_localidad(self):
        return self.__localidad

    def get_departamento_judicial(self):
        return self.__departamento_judicial

    def get_telefono(self):
        return self.__telefono

    def get_latitud(self):
        return self.__latitud

    def get_longitud(self):
        return self.__longitud

    def get_distancia(self, lat, lng):
        return ((self.__latitud - lat) ** 2 + (self.__longitud - lng) ** 2) ** 0.5


def obtener_datos(linea):
    datos = linea.split(";")
    #DATOS = N�mero;Fuero;Nombre;Tipo de ente;Direcci�n;Localidad;Departamento judicial;Tel�fono;Latitud;Longitud

    #DEVUELVO EL NUMERO DEL JUZAGADO Y UN OBJETO DE CLASE Dep_judicial con todos los datos
    return datos[0],Dep_judicial(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],float(datos[8].replace(",",".")),float(datos[9].replace(",",".")))

def obtener_departamentos_judiciales():
    archivo = open("mapa-judicial.csv", "r")
    departamentos_judiciales = {}
    linea = archivo.readline().replace("\n","") # DESCARTO LA PRIMERA LINEA QUE SON LOS TITULOS
    linea = archivo.readline().replace("\n","")
    while linea !="" :
        numero,departamento = obtener_datos(linea)
        departamentos_judiciales[numero] = departamento # ARMO UN DICCIONARIO QUE LA CLAVE SON LOS NUMEROS DE JUZGADOS Y GUARDO LOS OBJETOS DE CLASE Dep_judicial
        linea = archivo.readline().replace("\n","")
    return departamentos_judiciales # DEVUELVO EL DICCIONARIO

def calcular_departamento_cercano(latitud,longitud):
    dicc_departamentos = obtener_departamentos_judiciales()
    primera_vez = True
    for departamento in dicc_departamentos.keys(): # RECORRO EL DICCIONARIO DE JUZGADOS 
        distancia = dicc_departamentos[departamento].get_distancia(latitud,longitud) # CALCULO LA DISTANCIA DEL JUZGADO CON LA LATITUD Y LONGITUD PASADAS POR PARAMETRO
        if primera_vez: # SI ES EL PRIMER JUZGADO DE LA LISTA
            distancia_minima = distancia # GUARDO LA DISTANCIA
            departamento_cercano = departamento # GUARDO EL JUZGADO
            primera_vez = False
        elif distancia < distancia_minima: # SI LA DISTANCIA ES MENOR A LA DISTANCIA MAS CHICA
            distancia_minima = distancia # GUARDO LA DISTANCIA
            departamento_cercano = departamento # GUARDO EL JUZGADO
    return dicc_departamentos[departamento_cercano] # DEVUELVO EL OBJETO Dep_judicial



