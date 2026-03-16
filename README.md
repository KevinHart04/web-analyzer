#  Web Analyzer CLI

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Terminal-Rich-darkorange.svg?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Built with Rich">
  <img src="https://img.shields.io/badge/Estado-En%20Desarrollo%20Activo-success.svg?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Mantenimiento-Constante-blueviolet.svg?style=for-the-badge" alt="Maintenance">
</div>

<br>

**Web Analyzer CLI** es una herramienta de reconocimiento (*recon*) orientada a ciberseguridad y auditoría web, diseñada para ser ejecutada desde la terminal. Prioriza la velocidad, la modularidad y, sobre todo, una **experiencia visual impecable** gracias a una interfaz de usuario rica en colores y animaciones.

>  **Nota del Desarrollador:** Este proyecto es un organismo vivo. Está en **constante mejora y refactorización**. Nuevos módulos, capacidades de evasión y técnicas de escaneo se añaden regularmente.

---

## Características Actuales

- **Arquitectura Modular:** El núcleo de peticiones y los analizadores están separados, permitiendo escalar el script sin crear código espagueti.
- **Validación de Objetivos:** Comprobación de estado HTTP y manejo de *timeouts* antes de lanzar el análisis pesado.
- **Auditoría de Cabeceras (Headers):** Extracción y formateo en tablas de las cabeceras HTTP para identificar exposición de software y configuraciones de seguridad.
- **Cazador de `robots.txt`:** Búsqueda automática de rutas restringidas y exposición directa en terminal mediante paneles estilizados.
- **UI/UX en Consola:** Uso intensivo de `rich` para mostrar progreso en tiempo real (*spinners*), tablas y alertas con un esquema de colores de alto contraste.

---

## Instalación y Uso

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/web_analyzer.git](https://github.com/TU_USUARIO/web_analyzer.git)
   cd web_analyzer
   ```

2. **Instala las dependencias:**
   Se recomienda usar un entorno virtual (`venv`).
   ```bash
   pip install requests rich
   ```

3. **Ejecuta la herramienta:**
   Pásale el argumento requerido con la URL objetivo.
   ```bash
   python analyzer.py [https://ejemplo.com](https://ejemplo.com)
   ```

---

## Roadmap (Lo que se viene)

Al estar en constante evolución, estas son algunas de las características que están en el horno:

- [ ] **Fingerprinting:** Detección automática de CMS (WordPress, Moodle, etc.) y tecnologías subyacentes. *(En desarrollo)*
- [ ] **Fuerza bruta de directorios:** Búsqueda de rutas ocultas comunes (`/admin`, `.git`, etc.).
- [ ] **Soporte para múltiples hilos (Threading):** Para escaneos masivos en menor tiempo.
- [ ] **Exportación de reportes:** Guardar los resultados en formato JSON o Markdown.
- [ ] **Migración de argumentos:** Soporte completo para *flags* opcionales (ej. `-u`, `-t`, `-q`).

---

*Hecho con ☕ y código estructurado.*
