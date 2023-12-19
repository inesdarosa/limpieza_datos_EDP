''' Los nombres estan en distinta forma, están pegados, y hay casos
que siendo la misma persona están escritos diferentes. Esto es lo que 
quiero arreglar. '''

import numpy as np 
import pandas as pd 
import os
import re

os.chdir('G:/Mi unidad/proy_silvana/planillas/Insc_EVAI_CSV_2/inscripcion')

new_insc_general = pd.read_csv('new_insc_general.csv')
new_insc_general.columns.values


# Acá paso todos los 'Nombre y Apellido' a minúsculas:
cols_to_change = ['Nombre y Apellido']

for col in cols_to_change:
    new_insc_general['Nombre y Apellido'] = (new_insc_general['Nombre y Apellido']
                                             .str.lower())

new_insc_general['Nombre y Apellido']

# Ordeno el dataframe por el 'Nombre y Apellido'
new_insc_general_ordenada = new_insc_general.sort_values(by='Nombre y Apellido')

len(new_insc_general_ordenada['Nombre y Apellido'])
len(new_insc_general_ordenada)

new_insc_general_ordenada.to_csv('new_insc_general_1.csv')
new_insc_general_ordenada.columns.values
len(new_insc_general_ordenada['Cédula de Identidad'])-1


# después que ordené el dataframe por orden alfabético del nombre el 
# dataframe no reseteo el index, entonces tuve que resetearlo.

# para resetear el índdice:
new_insc_general_ordenada.reset_index(inplace=True)
new_insc_general_ordenada['Nombre y Apellido'].head(30)


# con este ciclo for, a través del número de cédula, arreglo el nombre
# de los estudiantes para que los que tengan el mismo número de cédula
# aparezcan con el mismo Nombre y Apellido

for i in range(len(new_insc_general_ordenada['Cédula de Identidad'])-1):
    
    if new_insc_general_ordenada['Cédula de Identidad'][i] == (new_insc_general_ordenada
    ['Cédula de Identidad'][i + 1]) and new_insc_general_ordenada['Nombre y Apellido'][i] != (
        new_insc_general_ordenada['Nombre y Apellido'][i + 1]):

        new_insc_general_ordenada['Nombre y Apellido'][i + 1] = (
            new_insc_general_ordenada['Nombre y Apellido'][i])

new_insc_general_ordenada['Nombre y Apellido'].head(30)

new_insc_general_ordenada.to_csv('new_insc_general_2.csv')


