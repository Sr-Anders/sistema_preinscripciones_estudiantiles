from fastapi import FastAPI # Importa la clase "FastAPI" desde la librería "fastapi" para crear la aplicación web.
from app.core.config import settings # Importa la instancia "settings" desde el módulo "app.core.config" para acceder a las variables de entorno y la URL de conexión a la base de datos

app= FastAPI(title=settings.PROJECT_NAME) # Crea una instancia de la clase "FastAPI" y asigna el nombre del proyecto desde las variables de entorno como título de la aplicación.

@app.get("/") # Define una ruta HTTP GET en la raíz ("/") de la aplicación.
def read_root(): # Define la función "read_root" que se ejecutará cuando se acceda a la ruta raíz ("/").
    print(f"Conectando a la base de datos en: {settings.database_url}") # Imprime en la consola la URL de conexión a la base de datos desde las variables de entorno.
    return {"message": f"Bienvenido a {settings.PROJECT_NAME}"} # Devuelve un diccionario con un mensaje de bienvenida que incluye el nombre del proyecto desde las variables de entorno.