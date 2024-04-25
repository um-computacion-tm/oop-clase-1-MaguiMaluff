import unittest
from materia_profesor import Materia, Profesor, Alumno

class TestMateria(unittest.TestCase):
    def test_init(self):
        materia = Materia("Computacion", None, None)
        self.assertEqual(materia.__nombre__, "Computacion")
        self.assertEqual(materia.__profesores__, None)
        self.assertEqual(materia.__alumnos__, None)
    
    def test_obtener_profesores(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        profesor_2 = Profesor("Carlos", "JTP", "679")
        materia = Materia("Computacion", [profesor_1, profesor_2], None)
        self.assertEqual(materia.obtener_profesores(), [profesor_1, profesor_2])

    def test_obtener_alumnos(self):
        alumno_1 = Alumno("Maria", "123", "maria@gmail.com")
        alumno_2 = Alumno("Carlos", "369", "carlos@gmail.com")
        materia = Materia("Computacion", None, [alumno_1, alumno_2],)
        self.assertEqual(materia.obtener_alumnos(), [alumno_1, alumno_2])


    def test_cambiar_nombre(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        materia = Materia("Computacion", [profesor_1], None)
        self.assertEqual(materia.__nombre__, "Computacion")
        materia.cambiar_nombre("Computacion 2")
        self.assertEqual(materia.__nombre__, "Computacion 2")

class TestProfesor(unittest.TestCase):
    def test_init(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        self.assertEqual(profesor_1.__nombre__, "Maria")
        self.assertEqual(profesor_1.__cargo__, "Titular")
        self.assertEqual(profesor_1.__legajo__, "123")
    
    def test_obtener_nombre(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        self.assertEqual(profesor_1.obtener_nombre(), "Maria")
    
    def test_obtener_cargo(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        self.assertEqual(profesor_1.obtener_cargo(), "Titular")
    
    def test_obtener_legajo(self):
        profesor_1 = Profesor("Maria", "Titular", "123")
        self.assertEqual(profesor_1.obtener_legajo(), "123")

class TestAlumno(unittest.TestCase):
    def test_init(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.__nombre__, "Maria")
        self.assertEqual(alumno.__legajo__, "123")
        self.assertEqual(alumno.__email__, "maria@gmail.com")

    def test_cambiar_nombre(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.__nombre__, "Maria")
        alumno.cambiar_nombre("Juana")
        self.assertEqual(alumno.__nombre__, "Juana")

    def test_cambiar_email(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.__email__, "maria@gmail.com")
        alumno.cambiar_email("m@gmail.com")
        self.assertEqual(alumno.__email__, "m@gmail.com")

    def test_obtener_nombre(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.obtener_nombre(), "Maria")
    
    def test_obtener_legajo(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.obtener_legajo(), "123")
    
    def test_obtener_email(self):
        alumno = Alumno("Maria", "123", "maria@gmail.com")
        self.assertEqual(alumno.obtener_email(), "maria@gmail.com")   

unittest.main()