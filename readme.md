# Descripción del Proyecto

Este proyecto es una aplicación en Python que lee un archivo ZIP, extrae uno de los archivos XLSX contenidos y lo convierte en un archivo CSV.

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