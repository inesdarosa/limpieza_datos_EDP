''' Necesito arreglar las edades de la tabla de inscripción general, pero
antes para poder comparar con las tablas por año que tienen las edades
correctas, tengo que igualarlas por el nombre, poner la misma columna nombre y 
appellido de las tablas individuales que las generales. Luego de hacer
esto, sí voy a ver como hago para arreglar las edades.

Espcificamnete acá creo un código para arreglar las edades que es testado
en la planilla de Inscripción. Además homogeneizo el nombre de los cursos
'''

import numpy as np 
import pandas as pd 
import os
import re
import unidecode

os.chdir('G:/Mi unidad/proy_silvana/planillas/Insc_EVAI_CSV_2/inscripcion')

Inscr_18_edad = pd.read_csv('Insc_2018_estimacion_edad.csv')
Inscr_18_edad.columns.values # devuelve el nombre de las columnas

Inscr_18_edad.count() # devuelve el numero de filas por columna

# junta dos columnas en una:
Inscr_18_edad['Nombre y Apellido'] = (Inscr_18_edad.Nombres.
                                      str.cat(Inscr_18_edad.Apellidos))


Inscr_18_edad.count()
Inscr_18_edad.head() # devuelve las primeras filas

for i in range(0, len(Inscr_18_edad['Nombre y Apellido'])):
    print (Inscr_18_edad['Nombre y Apellido'][i])


# Con esto elimino tildes, ñ y algún otro chirimbolo:
Inscr_18_edad['Nombre y Apellido'] = (Inscr_18_edad['Nombre y Apellido'].
                                      apply(lambda x: unidecode.unidecode(x)))

Inscr_18_edad.count()
Inscr_18_edad.head(10)

new_Inscr_18_edad = Inscr_18_edad.copy() # genera una copia del dataframe

Incsr_general = pd.read_csv('Copia_Incsr_18_19_20_21.csv')
Incsr_general.columns.values
len(Incsr_general['Nombre y Apellido'])
new_Incsr_general = Incsr_general.copy() # genera una copia del dataframe

new_Incsr_general['Nombre y Apellido'] = (new_Incsr_general['Nombre y Apellido'].
                                      apply(lambda x: unidecode.unidecode(x)))

# Voy a recorrer una columna y que printee el valor del dato

len(new_Inscr_18_edad['Nombre y Apellido']) # largo de la columna 'Nombre y Apellido'
new_Inscr_18_edad['Nombre y Apellido'][1] # devuelve el caso en la posición 1

new_Inscr_18_edad['Nombre y Apellido']
new_Inscr_18_edad.to_csv('new_Inscr_18_edad.csv')

# Este doble ciclo va examinando la matriz general por el nombre y la específica
# por año y cuando son iguales sustituye la edad de la general por la específica.
# Parece que funciona

for i in range(0, len(new_Incsr_general['Nombre y Apellido'])):
    
    for j in range(0, len(new_Inscr_18_edad)):

        if new_Incsr_general['Nombre y Apellido'][i] == (new_Inscr_18_edad
                                                         ['Nombre y Apellido'][j]):
            
            new_Incsr_general['EDAD'][i] = new_Inscr_18_edad['edad'][j]

            #print(new_Incsr_general['EDAD'][i], new_Inscr_18_edad['edad'][j])


#new_Incsr_general.to_csv('new_insc_general.csv')


# Ahora voy modificar el nombre de los cursos para homogeneizarlos

insc_cursos = pd.read_csv('insc_cursos_editado.csv')

new_Incsr_general.columns.values


for i in range(0, len(new_Incsr_general['Nombre del curso al que deseas inscribirte'])):

    for j in range(0, len(insc_cursos['cursos_originales'])):

        if new_Incsr_general['Nombre del curso al que deseas inscribirte'][i] == (
            insc_cursos['cursos_originales'][j]):

            new_Incsr_general['Nombre del curso al que deseas inscribirte'][i] = (
                insc_cursos['cursos_corregidos'][j])

new_Incsr_general['Nombre del curso al que deseas inscribirte'].head(10)

new_Incsr_general.to_csv('new_insc_general.csv')

len(new_Incsr_general)