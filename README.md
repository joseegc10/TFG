# Estimación de tipos de uso y coberturas del suelo mediante aprendizaje profundo e imágenes satélite

Este repositorio contiene los scripts que se han llevado a cabo para la elaboración del TFG de Ingeniería Informática de la Universidad de Granada.

En primer lugar, tenemos una serie de scripts en los que se desarrollan modelos de deep learning para la predicción de la cobertura terrestre. Estos son:

- **Modelo_Propio**: En él se prueba un modelo diseñado completamente por mi como primera toma de contacto de los datos que teníamos.
- **Modelo_MobileNet_FC**: En él se parte del modelo base llamado MobileNet y se congelan todas las capas en el entrenamiento menos las últimas completamente conectadas.
- **Modelo_MobileNet**: En él se parte del modelo base llamado MobileNet y se entrenan todas las capas.
- **Modelo_DenseNet**: En él se parte del modelo base llamado DenseNet y se entrenan todas las capas.

Después, tenemos un script llamado **createDataLabels** en el que se leen los datos desde una carpeta y se generan los arrays de datos y de etiquetas, almacenándolos en memoria.

También tenemos un script llamado **tifToJpeg** en el que pasamos una serie de imágenes en formato TIF a formato Jpeg.

Por último, nos encontramos un script llamado **predictionEarthEngine**, en el que generamos un mapa de cobertura terrestre haciendo uso de Google Earth Engine.
