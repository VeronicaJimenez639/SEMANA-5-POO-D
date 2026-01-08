"""
Servicio Registro: Administra una lista de estudiantes y permite registrar y consultar información.
"""

from modelos.estudiante import Estudiante   # Importa la clase Estudiante desde la carpeta modelos


class Registro:
    # Constructor: crea la lista donde se guardarán los estudiantes
    def __init__(self):
        self.estudiantes = []  # lista (tipo compuesto) para almacenar objetos Estudiante

    # Agrega un estudiante a la lista
    def agregar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)   # append agrega el elemento al final de la lista

    # Busca un estudiante por nombre (retorna el objeto o None)
    def buscar_por_nombre(self, nombre):
        for estudiante in self.estudiantes:                  # Revisa cada estudiante guardado en la lista
            if estudiante.nombre.lower() == nombre.lower():  # lower convierte a minúsculas para que la búsqueda no dependa de mayúsculas o tildes
                return estudiante
        return None

    # Calcula el promedio general de todos los estudiantes
    def calcular_promedio_general(self):
        if len(self.estudiantes) == 0:          # len devuelve cuántos estudiantes hay en la lista
            return 0.0            # Si no hay estudiantes, el promedio general se considera 0.0

        suma_promedios = 0.0                    # Variable float para acumular la suma de promedios
        for estudiante in self.estudiantes:     # Recorre todos los estudiantes del registro
            suma_promedios += estudiante.promedio  # Acumula el promedio de cada estudiante

        return suma_promedios / len(self.estudiantes)

    # Cuenta cuántos estudiantes son becados
    def contar_becados(self):
        contador_becados = 0    # Variable int para llevar el conteo de becados
        for estudiante in self.estudiantes:
            if estudiante.es_becado:         # Si es_becado es True, entra aquí
                contador_becados += 1        # Aumenta el contador en 1
        return contador_becados      # Devuelve el total de estudiantes becados
