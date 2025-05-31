# jobs-etl-g4

## Pipeline ETL para Extracción de Ofertas Laborales

Este proyecto implementa un pipeline ETL (Extracción, Transformación, Carga) para extraer ofertas laborales de LinkedIn, transformarlas y cargarlas en una base de datos MySQL. El pipeline está orquestado utilizando Prefect para una mejor gestión y monitoreo.

## Autor

Anderson Alarcon

## Requisitos

Asegúrate de tener instalado Python 3.x y pip.

## Configuración del Entorno

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/jobs-etl-g4.git
    cd jobs-etl-g4
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate     # En Windows
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuración de la Base de Datos MySQL

1.  **Crear la base de datos:**
    Debes crear una base de datos en MySQL Workbench (o tu cliente MySQL preferido) con el nombre `basedescrapping`.

    ```sql
    CREATE DATABASE basedescrapping;
    ```

2.  **Configurar credenciales:**
    Asegúrate de que las credenciales de la base de datos en `load.py` (`DB_CONFIG`) coincidan con tu configuración de MySQL. Por defecto, están configuradas para `user: 'root'` y `password: ''` (vacío).

    ```python
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': '',
        'database': 'basedescrapping'
    }
    ```

## Ejecución del Pipeline ETL

Para ejecutar el pipeline, simplemente ejecuta el archivo `main.py`:

```bash
python main.py
```

Esto ejecutará el flujo de Prefect, que realizará las siguientes operaciones:
1.  **Extracción:** Obtendrá las ofertas de trabajo de LinkedIn.
2.  **Transformación:** Procesará los datos extraídos (actualmente, esta etapa no realiza transformaciones complejas).
3.  **Carga:** Guardará las ofertas de trabajo en la tabla `jobs` de tu base de datos `basedescrapping`.

## Monitoreo con Prefect UI

Para monitorear tus flujos de Prefect, puedes iniciar la interfaz de usuario de Prefect:

```bash
prefect ui
```

Luego, abre tu navegador y ve a `http://localhost:4200` (o el puerto que indique la consola). Podrás ver el estado de tus ejecuciones de flujo, registros y más.

## Estructura del Proyecto

*   `extract.py`: Contiene la lógica para extraer datos de LinkedIn.
*   `transform.py`: Contiene la lógica para transformar los datos (actualmente una transformación de identidad).
*   `load.py`: Contiene la lógica para cargar los datos en MySQL.
*   `main.py`: El punto de entrada principal que define y ejecuta el flujo de Prefect.
*   `requirements.txt`: Lista de dependencias de Python.
*   `.gitignore`: Archivos y directorios a ignorar por Git.
