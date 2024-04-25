class Materia:
    def __init__(self, nombre, profesores, alumnos):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__
    
    def obtener_alumnos(self):
        return self.__alumnos__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre


class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__

class Alumno:
    def __init__(self, nombre, legajo, email):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__email__ = email
    
    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre
    
    def cambiar_email(self, email):
        self.__email__ = email
    
    def obtener_nombre(self):
        return self.__nombre__

    def obtener_legajo(self):
        return self.__legajo__
    
    def obtener_email(self):
        return self.__email__