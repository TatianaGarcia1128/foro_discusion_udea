# foro_discusion_udea
Proyecto de grado que implementa inteligencia artificial para el análisis de los datos de un foro de discusión de temas tecnológicos.

Para construir y desarrollar la información presentada en este repositorios se siguieron los siguientes pasos:

# Paso 1: Selección de tablas y campos
En los archivos 'selección de datos Discuss.excalidraw' o 'selección de datos Discuss.png' se encuentran las tablas y los campos resaltados en color azul a los cuales se le aplicará IA para cumplir los objetivos propuestos: <br>
1. Segmentar y clasificar a los usuarios que utilizan la herramienta de foro de discusión en la Vicepresidencia de Tecnología de la empresa.
2. Evaluar la calidad de las respuestas proporcionadas por los usuarios en el foro de discusión en la Vicepresidencia de Tecnología de la empresa.

El total de tablas presentes en la base de datos era de 114.

# Paso 2:  Ejecución de scripts en python
De acuerdo con los campos y tablas seleccionadas se diseña el query para extraer los datos en dos archivos que servirán para cumplir los objetivos propuestos. 
Dichos querys se encuentran en la carpeta 'procesar_querys'; teniendo en cuenta que previamente se había realizado la restauración de un backup de la base de datos hasta mayo del año 2023 y que contenía solo 'INSERTS'.
Por lo anterior, para ejecutar dichos querys es requerido restaurar este backup en una base de datos Postgres local la cual contiene información sensible como ips y servidores que no puede ser compartida en el repositorio. Sin embargo, se deja a modo de información las herramientas usadas para generar los archivos .csv que se usarán en el proyecto.

# Paso 3: Lectura de los data_preparation
En los archivos 'data_preparation_users' y 'data_preparation_posts' se encuentra la lectura de los dos dataset exportados y adjuntados en el repo 'dataset_posts.csv' y 'dataset_users.csv'.

# Pendientes
El archivo data_preparation_posts le hace falta hacer la limpieza adecuada; por el momento solo contiene la consulta de la información.



