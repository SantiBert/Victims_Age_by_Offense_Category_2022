# Proyecto de Scraping y Análisis de Datos

Este proyecto consiste en dos scripts en Python que realizan scraping de una página web para descargar datos y luego analizan esos datos para generar un archivo CSV.

## Archivos

1. **scrap.py**: Contiene funciones para realizar el scraping de una página web utilizando Selenium y descargar datos relevantes.

2. **crear_csv.py**: Extrae y convierte datos descargados en un archivo ZIP a un archivo CSV utilizando bibliotecas como pandas y openpyxl.

## Uso

1. Ejecuta `scrap.py` para realizar el scraping y descargar los datos en un archivo ZIP llamado `victims.zip`.

2. Después de la descarga, ejecuta `crear_csv.py` para extraer y convertir los datos del archivo ZIP a un archivo CSV llamado `Victims_Age_by_Offense_Category_2022.csv`.

3. Asegúrate de tener todas las dependencias instaladas. Puedes instalarlas ejecutando `pip install -r requirements.txt`.

## Requisitos

- Python 3.x
- Bibliotecas especificadas en `requirements.txt`

## Configuración

- Ajusta las rutas y configuraciones necesarias en los archivos según tus necesidades.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias, problemas o mejoras, no dudes en crear un problema o enviar una solicitud de extracción.


# Instrucciones de Uso

Siga estos pasos para configurar y ejecutar el proyecto en su entorno local:

1. Crear un Entorno Virtual

# Puede utilizar 'venv' para crear un entorno virtual
python -m venv env

# Activar el entorno virtual (en sistemas basados en Unix)
source venv/bin/activate

# Activar el entorno virtual (en sistemas basados en Windows)
.\venv\Scripts\activate


2. Instalar Dependencias
Asegúrese de que está en el entorno virtual antes de ejecutar este comando.

pip install -r requirements.txt

Esto instalará las dependencias necesarias para ejecutar el proyecto.

3. Ejecutar el Archivo main.py

python main.py

Este script realizará las siguientes acciones:

Leerá el archivo ZIP "victims.zip".
Extraerá elarchivo  "Victims_Age_by_Offense_Category_2022.xlsx" contenidos en el ZIP.
Convertirá el archivo XLSX en un archivo CSV, 'Victims_Age_by_Offense_Category_2022.csv'