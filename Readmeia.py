import openai
import asyncio
from github import Github
import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura la API Key de OpenAI y el token de GitHub
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

# Inicializa el cliente de GitHub y configura la API de OpenAI
g = Github(GITHUB_TOKEN)
openai.api_key = CHATGPT_API_KEY

# Función para recorrer todos los archivos y carpetas del repositorio
def get_repo_contents(repo, path=""):
    contents = repo.get_contents(path)
    files = []
    
    while contents:
        file_content = contents.pop(0)
        
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            files.append({
                'path': file_content.path,
                'url': file_content.download_url
            })
    
    return files

# Descarga y lee el contenido de cada archivo
def read_files(files):
    file_contents = {}
    
    for file in files:
        response = requests.get(file['url'])
        if response.status_code == 200:
            file_contents[file['path']] = response.text
        else:
            print(f"Error al leer el archivo {file['path']}")
    
    return file_contents

# Función asincrónica para generar el README usando la API de ChatGPT
async def generate_readme(file_contents):
    prompt_base = """
    ¡Hola! Por favor, comportate como un documentador de proyectos github profesional, Haz un NOMBRE DE PROYECTO, RESUMEN del proyecto, COMO FUNCIONA en caso haya tkinter, PROPOSITO, DEPENDENCIAS, CONFIGURACIÓN, INSTALACIÓN, POSIBLES MEJORES y más cosas sobre el proyecto, todo para un README de Github. Ademas de eso,
    analiza las capacidades técnicas clave y las características del proyecto y descríbelas en formato de tabla en Markdown:

    |      | Característica   | Resumen       |
    | :--- | :---:            | :---          |
    | ⚙️  | **Arquitectura**   | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🔩 | **Calidad del Código** | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 📄 | **Documentación**  | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🔌 | **Integraciones**  | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🧩 | **Modularidad**    | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🧪 | **Pruebas**        | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | ⚡️  | **Rendimiento**    | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🛡️ | **Seguridad**      | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 📦 | **Dependencias**   | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |
    | 🚀 | **Escalabilidad**  | <ul><li>Hecho 1</li><li>Hecho 2</li><li>Hecho 3</li></ul> |

    Esta tabla debe ser llenada con los datos que te daré a continuación, lo cual es un repositorio de github y sus archivos, revisalo y llena la tabla con lo que te parezca.
    Completa cada fila con información relevante sobre el código, como características de arquitectura, calidad del código, documentación, integraciones, modularidad, pruebas, rendimiento, seguridad, dependencias y escalabilidad.
    La información con la que llenaras la informacion es:
"""
    combined_text = prompt_base + "\n\n".join([f"{path}: {content[:200]}" for path, content in file_contents.items()])
    
    # Realiza la llamada a la API de ChatGPT con el contenido combinado como prompt
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in creating README files."},
            {"role": "user", "content": combined_text}
        ],
        max_tokens=1024,
        temperature=0.5
    )
    
    return response['choices'][0]['message']['content'].strip()

# Función principal asincrónica
async def main(repo_url):
    repo_name = repo_url.split('/')[-2] + '/' + repo_url.split('/')[-1]
    repo = g.get_repo(repo_name)
    files = get_repo_contents(repo)
    file_contents = read_files(files)
    readme_content = await generate_readme(file_contents)
    
    # Guarda el README generado en un archivo local
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    messagebox.showinfo("Éxito", "README generado y guardado como README.md")

# Función para ejecutar la función principal asincrónica desde Tkinter
def run_async_main(repo_url):
    asyncio.run(main(repo_url))

# Configuración de la interfaz Tkinter
root = tk.Tk()
root.title("Generador de README")
root.geometry("600x250")
root.configure(bg="#f4f4f9")

# Personalización de fuentes y colores
title_font = font.Font(family="Helvetica", size=14, weight="bold")
label_font = font.Font(family="Helvetica", size=10)
button_font = font.Font(family="Helvetica", size=10, weight="bold")

# Frame para centrar el contenido
frame = tk.Frame(root, bg="#ffffff", bd=2, relief="solid", padx=20, pady=20)
frame.pack(pady=20)

# Etiqueta y entrada para el enlace de GitHub
title_label = tk.Label(frame, text="Generador de README para Repositorios de GitHub", font=title_font, bg="#ffffff")
title_label.pack(pady=10)

label = tk.Label(frame, text="Ingrese el enlace del repositorio de GitHub:", font=label_font, bg="#ffffff")
label.pack(pady=5)

entry = tk.Entry(frame, width=50, font=label_font, relief="solid", bd=1)
entry.pack(pady=5)

# Botón para iniciar la generación del README
generate_button = tk.Button(frame, text="Generar README", font=button_font, bg="#4CAF50", fg="white", 
                            activebackground="#45a049", command=lambda: run_async_main(entry.get()))
generate_button.pack(pady=15, ipadx=10, ipady=5)

# Ejecuta la aplicación Tkinter
root.mainloop()
