from pydantic_settings import BaseSettings, SettingsConfigDict # from pydantic_settings import BaseSettings # Importa la clase base "BaseSettings" desde la librería "pydantic_settings" para definir y validar las variables de entorno de la aplicación (incluyendo las del archivo .env).
from urllib.parse import quote_plus # Importa la función "quote_plus" desde el módulo "urllib.parse" para codificar caracteres especiales en las variables de entorno, como el signo "@" en la contraseña de la base de datos.
class Settings(BaseSettings): # Define la clase "Settings" que hereda de "BaseSettings" para manejar la configuración de la aplicación.
    # Variables generales de la aplicación
    PROJECT_NAME: str # Define la variable de entorno "PROJECT_NAME" como una cadena de texto (str) para almacenar el nombre del proyecto.
    SECRET_KEY: str # Define la variable de entorno "SECRET_KEY" como una cadena de texto (str) para almacenar la clave secreta utilizada en la aplicación.
    
    #Variables de la base de datos
    DB_HOST: str # Define la variable de entorno "DB_HOST" como una cadena de texto (str) para almacenar la dirección del host de la base de datos.
    DB_PORT: int # Define la variable de entorno "DB_PORT" como un entero (int) para almacenar el puerto de conexión a la base de datos.
    DB_NAME: str # Define la variable de entorno "DB_NAME" como una cadena de texto (str) para almacenar el nombre de la base de datos.
    DB_USER: str # Define la variable de entorno "DB_USER" como una cadena de texto (str) para almacenar el nombre de usuario de la base de datos.
    DB_PASSWORD: str # Define la variable de entorno "DB_PASSWORD" como una cadena de texto (str)

    @property
    def database_url(self) -> str: # Define un método de propiedad "database_url" que devuelve la URL de conexión a la base de datos como una cadena de texto (str).
        encoded_password = quote_plus(self.DB_PASSWORD) # Codifica la contraseña de la base de datos utilizando la función "quote_plus" para manejar caracteres especiales.
        return f"mysql+pymysql://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}" # Devuelve la URL de conexión a la base de datos en el formato requerido por SQLAlchemy, incluyendo el usuario, contraseña codificada, host, puerto y nombre de la base de datos.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8") # Configura la clase "Settings" para que lea las variables de entorno desde el archivo ".env" con codificación UTF-8.
settings = Settings() # Crea una instancia de la clase "Settings" para acceder a las variables de entorno y la URL de conexión a la base de datos en otras partes de la aplicación.
