from faker import Faker
from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
import random

fake = Faker("es_ES")   # Datos en español
Faker.seed(42)

def generar_libros(n):
    """Genera n libros con datos aleatorios usando Faker."""
    libros = []
    for i in range(n):
        isbn = fake.isbn13()
        titulo = fake.sentence(nb_words=3).replace(".", "")
        autor = fake.name()
        libros.append(Libro(isbn, titulo, autor))
    return libros

def generar_estudiantes(n):
    """Genera n estudiantes con datos aleatorios usando Faker."""
    carreras = [
        "Ingenieria en Sistemas",
        "Ingenieria Industrial",
        "Contabilidad",
        "Administracion de Empresas",
        "Medicina"
    ]
    estudiantes = []
    for _ in range(n):
        cedula = fake.numerify(text="09########")
        nombre = fake.first_name()
        apellido = fake.last_name()
        carrera = random.choice(carreras)
        estudiantes.append(Estudiante(cedula, nombre, apellido, carrera))
    return estudiantes

def main():
    print("=" * 62)
    print("  SISTEMA DE GESTION DE BIBLIOTECA UNEMI")
    print("  Datos generados con Faker (aleatorios)")
    print("=" * 62)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")

    # Generar y registrar 5 libros aleatorios
    print("\n-- Registrando libros aleatorios (Faker) --")
    libros = generar_libros(10)
    for libro in libros:
        biblioteca.registrar_libro(libro)

    # Generar y registrar 3 estudiantes aleatorios
    print("\n-- Registrando estudiantes aleatorios (Faker) --")
    estudiantes = generar_estudiantes(20)
    for est in estudiantes:
        biblioteca.registrar_estudiante(est)

    print(f"\n{biblioteca}\n")

    # Realizar préstamos con datos aleatorios
    print("-- Realizando prestamos --")
    fecha_prestamo = "2026-04-28"
    fecha_devolucion = "2026-05-05"

    # Prestar 3 libros a distintos estudiantes
    for i in range(10):
        resultado = biblioteca.prestar_libro(
            libros[i].isbn,
            estudiantes[i % len(estudiantes)].cedula,
            fecha_prestamo,
            fecha_devolucion
        )
        print(resultado)

    # Intentar prestar libro ya prestado (RF-04)
    print("\n-- Validacion: prestamo de libro no disponible (RF-04) --")
    print(biblioteca.prestar_libro(
        libros[0].isbn,
        estudiantes[1].cedula,
        fecha_prestamo,
        fecha_devolucion
    ))

    # Consultar prestamos activos del primer estudiante
    print(f"\n-- Prestamos activos de {estudiantes[0].nombre} --")
    activos = biblioteca.consultar_prestamos_activos(estudiantes[0].cedula)
    for p in activos:
        print(f"  -> {p}")

    # Devolver un libro
    print("\n-- Registrando devolucion --")
    print(biblioteca.devolver_libro(libros[0].isbn, estudiantes[0].cedula))
    print(f"  Estado: {libros[0]}")

    print(f"\n{'=' * 62}")
    print(f"  {biblioteca}")
    print(f"{'=' * 62}")

if __name__ == "__main__":
    main()