# Entornos de Desarrollo — 1.º DAM

Repositorio principal del módulo de Entornos de Desarrollo.

## Contenidos principales

- Python y organización de proyectos.
- Git y GitHub.
- Ramas, fusiones y resolución de conflictos.
- Testing con `unittest`.
- Cobertura de código.
- Refactorización.
- Documentación técnica.
- GitHub Classroom.

## Objetivos

- Mantener los materiales docentes versionados.
- Centralizar teoría, actividades, proyectos y evaluación.
- Aplicar Git en el propio desarrollo de los materiales.
- Trabajar con proyectos reproducibles.
- Reutilizar la información para la programación didáctica.

## Organización del repositorio

Cada tema contiene una carpeta por actividad. Cada actividad guarda únicamente
los archivos finales necesarios y un `solucion.md` con los pasos, comandos,
cambios de código y respuestas a todas las partes del enunciado.

```text
tema-03-git/src/actividades/
├── actividad01/    # agenda.py y solucion.md
├── actividad02/    # conversor.py y solucion.md
├── actividad03/    # incidencias.py y solucion.md
├── actividad04/    # reservas.py y solucion.md
├── actividad05/    # calculadora.py y solucion.md
├── actividad06/    # pedido.py, verificar.py y solucion.md
└── actividad07/    # biblioteca.py, verificar_integracion.py y solucion.md
```

### Tema 3 — Comandos básicos de Git

| Actividad | Pasos y solución |
| --- | --- |
| 1. Agenda: primeros commits | [solucion.md](tema-03-git/src/actividades/actividad01/solucion.md) |
| 2. Conversor: preparación selectiva e ignorados | [solucion.md](tema-03-git/src/actividades/actividad02/solucion.md) |
| 3. Incidencias: restore, amend y reset | [solucion.md](tema-03-git/src/actividades/actividad03/solucion.md) |
| 4. Reservas: revert | [solucion.md](tema-03-git/src/actividades/actividad04/solucion.md) |
| 5. Calculadora: ramas y fusiones | [solucion.md](tema-03-git/src/actividades/actividad05/solucion.md) |
| 6. Pedidos: conflictos entre tres ramas | [solucion.md](tema-03-git/src/actividades/actividad06/solucion.md) |
| 7. Biblioteca: integración por fases | [solucion.md](tema-03-git/src/actividades/actividad07/solucion.md) |

Los documentos explican cómo realizar las prácticas manualmente en Ubuntu,
editando con PyCharm. Los comandos Git se ejecutan en repositorios nuevos,
como pide el enunciado. Para ejecutar solamente el resultado final basta abrir
el archivo Python correspondiente en PyCharm o usar `python3 ruta/al/archivo.py`.
Los verificadores de las actividades 6 y 7 conservan el contenido del enunciado.

## Curso actual

2026-2027
