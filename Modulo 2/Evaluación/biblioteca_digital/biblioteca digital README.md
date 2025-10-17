# Sistema de Gestión de Biblioteca Digital

Este proyecto es una aplicación de consola en Python para gestionar libros, usuarios y préstamos de la "Biblioteca Digital para Ingenieros de Datos" de DataSolutions Academy.

## Características

- **Gestión de Libros**: Registrar y consultar libros por autor, género o disponibilidad.
- **Gestión de Usuarios**: Registrar usuarios con diferentes roles (Estudiante, Instructor) usando herencia.
- **Gestión de Préstamos**: Realizar préstamos validando la disponibilidad del libro y la existencia del usuario.
- **Manejo de Errores**: Uso de excepciones personalizadas para un control robusto de errores comunes.
- **Estructura Modular**: El código está organizado en un paquete de Python (`biblioteca`).
- **Principios de POO**: Aplicación de clases, objetos, herencia y polimorfismo.

## Estructura de Archivos

biblioteca_digital/
│
├── biblioteca/
│ ├── __init__.py
│ ├── libros.py
│ ├── usuarios.py
│ ├── prestamos.py
│ ├── excepciones.py
│ ├── gestion_libros.py
│ ├── gestion_usuarios.py
│ └── gestion_prestamos.py
│
├── main.py
└── README.md

