# faker_datos.py

from faker import Faker
import random
from modelo.libro import Libro
from modelo.estudiante import Estudiante

fake = Faker('es_ES')  # Nombres y datos en español

# ── Listas personalizadas ──────────────────────────────────────
CARRERAS = [
    "Ingeniería en Sistemas",
    "Ingeniería Industrial",
    "Ingeniería Civil",
    "Medicina",
    "Derecho",
    "Administración de Empresas",
    "Contabilidad y Auditoría",
    "Psicología",
    "Arquitectura",
    "Ingeniería Eléctrica",
]

TITULOS = [
    "Fundamentos de Programación",
    "Cálculo Diferencial e Integral",
    "Historia del Ecuador",
    "Introducción a la Física",
    "Química General",
    "Álgebra Lineal",
    "Estadística y Probabilidades",
    "Ética Profesional",
    "Economía General",
    "Estructuras de Datos",
    "Base de Datos Relacionales",
    "Redes de Computadores",
]

# ── Generadores ────────────────────────────────────────────────
def generar_libros(cantidad: int = 5) -> list:
    """Genera libros aleatorios con Faker."""
    libros = []
    for _ in range(cantidad):
        libro = Libro(
            isbn=fake.isbn13(),
            titulo=random.choice(TITULOS),
            autor=fake.name()
        )
        libros.append(libro)
    return libros


def generar_estudiantes(cantidad: int = 5) -> list:
    """Genera estudiantes aleatorios con Faker (cédulas únicas)."""
    estudiantes = []
    cedulas_usadas = set()

    while len(estudiantes) < cantidad:
        cedula = fake.numerify('09########')  # formato cédula Ecuador (provincia Guayas)
        if cedula not in cedulas_usadas:     # evita cédulas duplicadas
            cedulas_usadas.add(cedula)
            estudiante = Estudiante(
                cedula=cedula,
                nombre=fake.first_name(),
                apellido=fake.last_name(),
                carrera=random.choice(CARRERAS)
            )
            estudiantes.append(estudiante)

    return estudiantes