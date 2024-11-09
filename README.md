# NOMBRE DE PROYECTO
GitHub Assistant

## RESUMEN
GitHub Assistant es una herramienta que integra funcionalidades de GitHub con OpenAI y otras APIs para asistir en la gestión de repositorios y proyectos en GitHub.

## COMO FUNCIONA
El proyecto utiliza la librería `openai` para integrar capacidades de inteligencia artificial, `PyGithub` para interactuar con la API de GitHub, y `requests` para realizar solicitudes HTTP. Además, hace uso de `python-dotenv` para cargar variables de entorno desde un archivo `.env`. Para la interfaz gráfica, se emplea `tkinter`.

## PROPOSITO
El propósito de GitHub Assistant es facilitar tareas comunes de gestión de repositorios en GitHub, como la creación de problemas, la revisión de solicitudes de extracción y la generación de informes automatizados.

## DEPENDENCIAS
- openai==0.28.0
- PyGithub==2.5.0
- requests==2.31.0
- python-dotenv==1.0.1

## CONFIGURACIÓN
Antes de ejecutar el proyecto, asegúrate de crear un archivo `.env` con las siguientes variables:
```
GITHUB_TOKEN=your_github_token
CHATGPT_API_KEY=your_chatgpt_api_key
```

## INSTALACIÓN
1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Configura las variables de entorno en un archivo `.env`.
4. Ejecuta el archivo principal `Readmeia.py`.

## POSIBLES MEJORES
- Implementar más funcionalidades de interacción con la API de GitHub.
- Mejorar la interfaz gráfica para una experiencia de usuario más intuitiva.
- Añadir soporte para más servicios de inteligencia artificial.

## Capacidades Técnicas Clave

|      | Característica       | Resumen                                                                                   |
| :--- | :---:                | :---                                                                                      |
| ⚙️   | **Arquitectura**      | <ul><li>Integración de OpenAI y PyGithub</li><li>Interfaz gráfica con tkinter</li></ul>   |
| 🔩   | **Calidad del Código**| <ul><li>Uso de librerías reconocidas y actualizadas</li><li>Separación de funciones</li></ul> |
| 📄   | **Documentación**     | <ul><li>Comentarios detallados en el código</li><li>README completo</li></ul>            |
| 🔌   | **Integraciones**     | <ul><li>Integración con OpenAI y GitHub API</li><li>Uso de dotenv para variables de entorno</li></ul> |
| 🧩   | **Modularidad**       | <ul><li>División clara de funciones y componentes</li><li>Reutilización de código</li></ul> |
| 🧪   | **Pruebas**           | <ul><li>Implementación de pruebas unitarias y de integración</li><li>Validación de datos de entrada</li></ul> |
| ⚡️   | **Rendimiento**       | <ul><li>Optimización de solicitudes HTTP</li><li>Manejo eficiente de recursos</li></ul> |
| 🛡️   | **Seguridad**         | <ul><li>Uso de variables de entorno para datos sensibles</li><li>Validación de inputs</li></ul> |
| 📦   | **Dependencias**      | <ul><li>Control de versiones de las dependencias</li><li>Archivo `requirements.txt` actualizado</li></ul> |
| 🚀   | **Escalabilidad**     | <ul><li>Posibilidad de añadir más funcionalidades sin afectar la estructura actual</li><li>Manejo de errores y excepciones</li></ul> |