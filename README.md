# POO-Tarea01-Biblioteca-David-Jumbo

## Información del Estudiante
- **Nombre:** David Jumbo
- **Asignatura:** Programación Orientada a Objetos
- **Universidad:** Universidad Estatal de Milagro - UNEMI
- **Semestre:** [Tu semestre]

## Descripción del Proyecto
Sistema de Gestión de Biblioteca Universitaria implementado en Python
aplicando los 4 pilares de la Programación Orientada a Objetos.

## Estructura del Caso de Estudio

### Clases del Sistema
| Clase | Descripción | Relación |
|---|---|---|
| `Persona` | Clase base con cédula, nombre y apellido | Base (herencia) |
| `Estudiante` | Hereda de Persona, agrega carrera | Hereda de Persona |
| `Libro` | Gestiona ISBN, título, autor y disponibilidad | Composición con Biblioteca |
| `Prestamo` | Asocia un libro con un estudiante | Asociación |
| `Biblioteca` | Clase gestora principal del sistema | Contiene todo |

### Pilares POO aplicados
- **Abstracción:** Solo se modelan los atributos relevantes de cada entidad
- **Encapsulamiento:** Atributos privados con prefijo `_`, acceso mediante `@property`
- **Herencia:** `Estudiante` hereda de `Persona` usando `super().__init__()`
- **Polimorfismo:** El método `__str__()` se redefine en cada clase

### Requerimientos cumplidos
- RF-01: Registrar libros
- RF-02: Registrar estudiantes  
- RF-03: Registrar préstamos
- RF-04: Validar disponibilidad antes de prestar
- RF-05: Registrar devolución de libro
- RF-06: Consultar préstamos activos

## Ejecución
```bash
python main.py
```

## Estructura del Proyecto