from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca

def main():
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    print("── Registrando libros ──")
    libro1 = Libro("978-0-13-468599-1", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("978-0-06-112008-4", "Cien Años de Soledad", "Gabriel García Márquez")
    libro3 = Libro("978-84-376-0494-7", "Don Quijote de la Mancha", "Miguel de Cervantes")
    biblioteca.registrar_libro(libro1)
    biblioteca.registrar_libro(libro2)
    biblioteca.registrar_libro(libro3)

    print("\n── Registrando estudiantes ──")
    est1 = Estudiante("0926400615", "María", "López", "Ingeniería en Sistemas")
    est2 = Estudiante("0912345678", "Carlos", "Ramírez", "Ingeniería Industrial")
    est3 = Estudiante("0987971955", "David", "Jumbo", "Ingeniería en Software")
    biblioteca.registrar_estudiante(est1)
    biblioteca.registrar_estudiante(est2)
    biblioteca.registrar_estudiante(est3)

    print(f"\n{biblioteca}\n")

    print("── Realizando préstamos ──")
    print(biblioteca.prestar_libro("978-0-13-468599-1", "0926400615", "2026-04-18", "2026-04-26"))
    print(biblioteca.prestar_libro("978-0-06-112008-4", "0926400615", "2026-04-18", "2026-05-01"))
    print(biblioteca.prestar_libro("978-84-376-0494-7", "0912345678", "2026-04-18", "2026-04-22"))

    print("\n── Intentando prestar libro ya prestado ──")
    print(biblioteca.prestar_libro("978-0-13-468599-1", "0912345678", "2026-04-18", "2026-04-30"))

    print("\n── Préstamos activos de María López ──")
    for p in biblioteca.consultar_prestamos_activos("0926400615"):
        print(f"  → {p}")

    print("\n── Devolviendo un libro ──")
    print(biblioteca.devolver_libro("978-0-13-468599-1", "0926400615"))
    print(f"\n── Estado del libro devuelto ──\n  {libro1}")

    print("\n── Préstamos activos de María (después de devolución) ──")
    activos = biblioteca.consultar_prestamos_activos("0926400615")
    for p in activos:
        print(f"  → {p}")
    if not activos:
        print("  (Sin préstamos activos para este libro)")

    print(f"\n{'=' * 60}\n  {biblioteca}\n{'=' * 60}")

if __name__ == "__main__":
    main()