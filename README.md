# Proyecto-MD

Este proyecto contiene análisis exploratorio de datos sobre defunciones en México, específicamente sobre la edad, la causa de muerte y el sexo de los fallecidos.

## Contenido

En la carpeta `data` se encuentran los archivos CSV con los datos de defunciones separados por año, desde el 2009 hasta el 2019.

En la carpeta `tools` se encuentran los scripts de Python que se utilizaron para la preparación de los datos. Estos scripts se ejecutaron en el siguiente orden:

1. `deleter.py`: Este script se utilizó para eliminar hojas innecesarias de los archivos de Excel, dejando solamente la hoja de "Edad causa de muerte y sexo" para cada año.

2. `converterFromXls-Xlsx-to-csv.py`: Este script se utilizó para convertir los archivos de Excel a formato CSV.

3. `organizer.py`: Este script se utilizó para mover los archivos de Excel que no se convirtieron a CSV a una carpeta llamada "not converted".

4. `clean-column.py`: Este script se utilizó para eliminar una columna considerada irrelevante de los archivos CSV.

5. `combine_csv.py`: Este script se utilizó para combinar todos los archivos CSV en uno solo, agregando una columna "año_info" que indica a qué año pertenece cada fila.

## Uso

Para ejecutar los scripts, es necesario tener instalado Python 3.x y las bibliotecas Pandas y openpyxl. Se recomienda instalar las bibliotecas con el siguiente comando:


Para ejecutar cada script, se recomienda colocar el archivo a ejecutar en el directorio raíz del proyecto y modificar el path en el script para que apunte a la carpeta correspondiente. También se puede modificar la variable `directory` en cada script para que apunte a la carpeta correspondiente.

Una vez ejecutados los scripts, se obtendrá un archivo CSV llamado `defunciones_combinadas.csv` en la carpeta `data`, que contiene todos los datos de defunciones desde el 2009 hasta el 2019 en un solo archivo.

## Contribuyendo

Si deseas contribuir al proyecto, ¡estamos abiertos a colaboraciones! Siéntete libre de hacer un fork del repositorio y enviar tus pull requests.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
