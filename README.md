# ExamenSirenas
Tercer desafio de TrueHome

# Como ejecutar el codigo
El script ejecutable "main.py" se encuentra en la carpeta: "ExamenSirenas/src/main.py"

# Ver archivo "sirenas_endemicas_y_sirenas_migrantes.csv"
Este archivo contiene las sirenas que se buscan clasificar, si son endemicas o migrantes.  
El archivo tiene una columna que se llama "especie", en esta se observa para cada sirena cual es la predicion que se asocia a la clase que pertenece.  
- El archivo se localiza en la siguietne ruta "ExamenSirenas/data/".

# Seleccion de algoritmo de clasificacion
Se pueden seleccionar varios algoritmos de clasificacion para obtener a que clase pertenecen las sirenas.  
 Algoritmos:  
  - NearestCentroid
  - MLPClassifier
  - SGDClassifier
  - LogisticRegression
  - SVC1   <>
  - SVC2
  - DecisionTree
  - RandomForest  

Para probar algun algoritmo, hay que modificar la variable <MODEL> que se encuentra dentro del archivo "config.py" ubicado en "ExamenSirenas/src/".  
 - NOTA: el valor (puesto entre comillas "") que se le pasa a la variable es alguno de los nombre de algoritmos enlistados arriba, por ejemplo: **MODELO = 'RandomForest'**



En la carpeta "ExamenVeneno/plots/" se guardan las graficas de  dispersion y grafica de barra para cada caracteristica de veneno.  
Tambien se guarda una grafica de barras que muestra el total de instancias que cumplen el requisito en cada caracteristica para ser consideradas como sustancias toxicas.  
Por ultimo, tambien se genera una grafica de distribucion de las 10 caracteristicas.
