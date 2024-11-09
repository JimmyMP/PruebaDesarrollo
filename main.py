import openai
import asyncio
from github import Github
import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configura tu token de acceso de GitHub y la API Key de ChatGPT
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
REPO_URL = 'https://github.com/JimmyMP/TeamManufacturing.github.io'
REPO_NAME = REPO_URL.split('/')[-2] + '/' + REPO_URL.split('/')[-1]  # Extrae el nombre del repo

# Inicializa el cliente de GitHub y configura la API de OpenAI
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)
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
    ¡Hola! Por favor, Haz un resumen del proyecto, Titulos, Dependencias, Configuración, y más cosas sobre el proyecto. Ademas de eso,
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
    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(combined_text)
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
async def main():
    files = get_repo_contents(repo)
    print(files)
    file_contents = read_files(files)
    # Llama a `generate_readme` usando await
    readme_content = await generate_readme(file_contents)
    
    # Guarda el README generado en un archivo local
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README generado y guardado como README.md")

# Ejecuta la función principal asincrónica
asyncio.run(main())
