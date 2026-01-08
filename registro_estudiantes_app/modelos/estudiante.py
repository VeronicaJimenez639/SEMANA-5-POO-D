"""
Modelo Estudiante: Representa un estudiante con datos básicos usando tipos: str, int, float, bool.
"""

class Estudiante:
    # Constructor: se ejecuta al crear un objeto Estudiante()
    def __init__(self, nombre, edad, promedio, es_becado):
        self.nombre = nombre          # str: nombre del estudiante
        self.edad = edad              # int: edad en años
        self.promedio = promedio      # float: promedio (ej. 8.75)
        self.es_becado = es_becado    # bool: True/False

    # Método para devolver el estudiante como texto para imprimirlo
    def __str__(self):
        beca_texto = "Sí" if self.es_becado else "No"
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, promedio={self.promedio}, becado={beca_texto})"
