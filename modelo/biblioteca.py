from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.prestamo import Prestamo

class Biblioteca:
    """Gestiona libros, estudiantes y préstamos."""

    def __init__(self, nombre: str):
        self._nombre = nombre
        self._libros = []
        self._estudiantes = []
        self._prestamos = []

    def registrar_libro(self, libro: Libro) -> None:
        self._libros.append(libro)
        print(f"  ✓ Libro registrado: {libro.titulo}")

    def registrar_estudiante(self, estudiante: Estudiante) -> None:
        self._estudiantes.append(estudiante)
        print(f"  ✓ Estudiante registrado: {estudiante.nombre} {estudiante.apellido}")

    def _buscar_libro(self, isbn: str):
        for libro in self._libros:
            if libro.isbn == isbn:
                return libro
        return None

    def _buscar_estudiante(self, cedula: str):
        for estudiante in self._estudiantes:
            if estudiante.cedula == cedula:
                return estudiante
        return None

    def prestar_libro(self, isbn: str, cedula: str,
                      fecha_prestamo: str, fecha_devolucion: str) -> str:
        libro = self._buscar_libro(isbn)
        if libro is None:
            return f"  ✗ Error: No se encontró el libro con ISBN {isbn}"
        estudiante = self._buscar_estudiante(cedula)
        if estudiante is None:
            return f"  ✗ Error: No se encontró el estudiante con cédula {cedula}"
        if not libro.disponible:
            return f"  ✗ Error: El libro '{libro.titulo}' no está disponible"
        libro.prestar()
        prestamo = Prestamo(libro, estudiante, fecha_prestamo, fecha_devolucion)
        self._prestamos.append(prestamo)
        return f"  ✓ Préstamo registrado: '{libro.titulo}' → {estudiante.nombre}"

    def devolver_libro(self, isbn: str, cedula: str) -> str:
        for prestamo in self._prestamos:
            if (prestamo.libro.isbn == isbn and
                prestamo.estudiante.cedula == cedula and
                prestamo.activo):
                prestamo.registrar_devolucion()
                return f"  ✓ Devolución registrada: '{prestamo.libro.titulo}'"
        return "  ✗ Error: No se encontró un préstamo activo con esos datos"

    def consultar_prestamos_activos(self, cedula: str) -> list:
        return [p for p in self._prestamos
                if p.estudiante.cedula == cedula and p.activo]

    def __str__(self) -> str:
        return (f"Biblioteca '{self._nombre}' | "
                f"Libros: {len(self._libros)} | "
                f"Estudiantes: {len(self._estudiantes)} | "
                f"Préstamos: {len(self._prestamos)}")