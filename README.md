# foro_discusion_udea
Proyecto de grado que implementa inteligencia artificial para el análisis de los datos de un foro de discusión de temas tecnológicos.

Este proyecto incluye dos archivos Jupyter Notebook (.ipynb) que realizan análisis de datos utilizando datos almacenados en dos archivos CSV.

## Instrucciones de ejecución
### Paso 1: Requisitos previos
Asegúrate de tener instalado Python, Jupyter Notebook y Visual Studio Code en tu entorno. Puedes instalarlos ejecutando:

```bash
pip install jupyter
```

### Paso 2: Descargar el repositorio

```bash
git clone https://github.com/TatianaGarcia1128/foro_discusion_udea.git
```

### Paso 3: Ejecutar los Notebooks  
Abre Visual Studio Code, selecciona la opción: Archivo/Abrir carpeta y busca la carpeta donde se encuentra el proyecto clonado anteriormente.

Ejecutar cada uno de los pasos de cada notebook en orden secuencial. En caso que se presente errores por librerías que faltan; se deben instalar usando el comando (Ejemplo):

```bash
pip install bs4
```

**Importante:** 
- Para el notebook de preparación de datos del post 'data_preparationÑ_posts.ipynb' es indispensable instalar las siguientes librerías para que sea ejecutada sin errores la línea de limpieza de etiquetas html:

    ```bash
    pip install bs4
    pip install html5lib
    pip install lxml
    ```

- Igualmente se debe instalar la siguiente librería usada para la tokenización:

    ```bash
    pip install nltk scikit-learn
    ```

Posterior a su instalación reiniciar el IDE Visual Studio Code.


### Estructura del proyecto
- `data_preparation_users`: Notebook para el análisis de datos utilizando `dataset_users.csv`.
- `data_preparation_posts`: Notebook para el análisis de datos utilizando `dataset_posts.csv`.


### Notas adicionales

Como parte de las actividades realizadas previamente para obtener los archivos .csv con la data cruda que se usará para este proyecto, se incluyen en el proyecto a modo de complemente e informativo más NO hacen parte o son un requisito para la ejecución de este proyecto.

En la carpeta `diagramas_seleccion_data` se incluye una imagen creada en excalidraw para visualizar las tablas y campos seleccionados para ser trabajados en el proyecto del total de 114 tablas que se tenían.

En la carpeta `procesar_querys` se incluyen uno script en python que fueron usados para exportar los archivos .csv.




