"""
Tarea: Tipos de datos e identificadores.
Programa que registra estudiantes usando:
- str (nombre)
- int (edad)
- float (promedio)
- bool (es_becado)
Además aplica identificadores en snake_case y comentarios.
"""

from modelos.estudiante import Estudiante  # Importa la clase Estudiante desde la carpeta modelos
from servicios.registro import Registro    # Importa la clase Registro desde la carpeta servicios


def main():
    # Creamos el servicio de registro que guardará la lista de estudiantes
    registro = Registro()

    # Creamos estudiantes (usando distintos tipos de datos)
    estudiante_1 = Estudiante(nombre="Verónica", edad=19, promedio=8.75, es_becado=True)
    estudiante_2 = Estudiante(nombre="Carlos", edad=21, promedio=7.90, es_becado=False)
    estudiante_3 = Estudiante(nombre="Ana", edad=20, promedio=9.10, es_becado=True)

    # Agregamos estudiantes al registro
    registro.agregar_estudiante(estudiante_1)
    registro.agregar_estudiante(estudiante_2)
    registro.agregar_estudiante(estudiante_3)

    # Mostramos estudiantes registrados
    print("LISTA DE ESTUDIANTES")
    print(estudiante_1)
    print(estudiante_2)
    print(estudiante_3)

    # Buscamos un estudiante por nombre
    nombre_buscado = "Verónica"  # str
    estudiante_encontrado = registro.buscar_por_nombre(nombre_buscado) 

    print("\nBÚSQUEDA")
    if estudiante_encontrado is not None:
        print(f"Estudiante encontrado: {estudiante_encontrado}")   # Si encuentra al estudiante, devuelve el objeto Estudiante
    else:
        print("Estudiante no encontrado")      # Si no lo encuentra, devuelve None

    # Calculamos estadísticas del registro
    promedio_general = registro.calcular_promedio_general()  # float, promedio de todos los estudiantes
    total_becados = registro.contar_becados()                # int, total de estudiantes becados

    print("\nESTADÍSTICAS")
    print(f"Promedio general del curso: {promedio_general:.2f}") # Formatea el float a 2 decimales
    print(f"Total de estudiantes becados: {total_becados}")


# Punto de entrada del programa
if __name__ == "__main__":   # Si este archivo es el principal se ejecuta main()
    main()