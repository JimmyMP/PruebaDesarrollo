# Planificación de la demanda de tallarines Don Vittorio

---

## Resumen del Proyecto

El proyecto "Planificación de la demanda de tallarines Don Vittorio" se enfoca en predecir la demanda de productos de la empresa Don Vittorio utilizando modelos de series temporales. Se utiliza la metodología SARIMA para realizar estas predicciones, lo que permite a la empresa planificar de manera más efectiva su producción y distribución.

---

## Archivos y Dependencias

- **Archivos:**
  - `app.py`: Contiene el código principal de la aplicación web que permite visualizar y analizar las predicciones de la demanda.
  - `matos.py`: Archivo con funciones relacionadas a los modelos SARIMA y métricas de evaluación.
  - `data.csv`, `observado_vs_predicho.csv`, `optimized_data.csv`: Archivos de datos utilizados para el análisis y las predicciones.
  - `prediccion_demanda_don_vittorio_tallarin.py`: Script para realizar las predicciones de demanda.
  - `templates/index.html`: Archivo HTML para la interfaz de usuario de la aplicación web.
  - `static/css/style.css`: Hoja de estilos para la interfaz de usuario.
  - `static/images/`: Contiene imágenes utilizadas en la interfaz.
  - `static/js/script.js`: Script JavaScript para funcionalidades adicionales en la interfaz.
  - `static/uploads/`: Directorio para subir archivos de datos.

- **Dependencias:**
  - Flask==3.0.3
  - gunicorn==20.1.0
  - numpy==1.26.4
  - pandas==2.2.2
  - matplotlib==3.9.0
  - statsmodels==0.14.2
  - scikit-learn==1.5.0
  - openpyxl==3.1.3

---

## Capacidades Técnicas Clave

|      | Característica       | Resumen                                                                                   |
| :--- | :---:                | :---                                                                                      |
| ⚙️   | **Arquitectura**      | Implementación de modelos SARIMA para predecir la demanda.                                |
| 🔩   | **Calidad del Código** | Utilización de buenas prácticas de Python y estructuración modular.                       |
| 📄   | **Documentación**     | Documentación clara y detallada de los scripts y funciones utilizadas.                    |
| 🔌   | **Integraciones**     | Integración con Flask para desplegar una interfaz web interactiva.                        |
| 🧩   | **Modularidad**       | Código modularizado para facilitar mantenimiento y escalabilidad.                        |
| 🧪   | **Pruebas**           | Implementación de pruebas unitarias para validar la precisión de los modelos de predicción. |
| ⚡️   | **Rendimiento**       | Optimización de los modelos para lograr predicciones rápidas y precisas.                  |
| 🛡️   | **Seguridad**         | Implementación de medidas de seguridad para proteger los datos sensibles de la empresa.   |
| 📦   | **Dependencias**      | Gestión de dependencias actualizada y controlada para garantizar la estabilidad del proyecto. |
| 🚀   | **Escalabilidad**     | Diseño y estructura preparados para escalabilidad en caso de aumentar la demanda de procesamiento. |

--- 

Este resumen destaca las principales características y capacidades técnicas del proyecto "Planificación de la demanda de tallarines Don Vittorio", mostrando su enfoque en la predicción de la demanda de productos de la empresa mediante modelos de series temporales y su implementación a través de una aplicación web interactiva.