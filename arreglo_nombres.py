''' Los nombres estan en distinta forma, están pegados, y hay casos
que siendo la misma persona están escritos diferentes. Esto es lo que 
quiero arreglar. '''

import numpy as np 
import pandas as pd 
import os
import re
import unidecode

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


# Lo que sigue para EVALUACION

os.chdir('G:/Mi unidad/proy_silvana/planillas/Insc_EVAI_CSV_2/evaluacion')

Eval_18_19_20_21_mod = pd.read_csv('Eval_18_19_20_21_mod.csv')
Eval_18_19_20_21_mod.columns.values

# Con esto elimino tildes, ñ y algún otro chirimbolo:
Eval_18_19_20_21_mod['Nombre y Apellido'] = (Eval_18_19_20_21_mod['Nombre y Apellido'].
                                      apply(lambda x: unidecode.unidecode(x)))


# Acá paso todos los 'Nombre y Apellido' a minúsculas:
cols_to_change = ['Nombre y Apellido']

for col in cols_to_change:
    Eval_18_19_20_21_mod['Nombre y Apellido'] = (Eval_18_19_20_21_mod['Nombre y Apellido']
                                             .str.lower())



# con este ciclo for, a través del email, arreglo el nombre
# de los estudiantes para que los que tengan el mismo email
# aparezcan con el mismo Nombre y Apellido

len(Eval_18_19_20_21_mod['Dirección de correo electrónico'])
Eval_18_19_20_21_mod['Nombre y Apellido'].head(30)
Eval_18_19_20_21_mod['Nombre y Apellido'].tail(30)

for i in range(len(Eval_18_19_20_21_mod['Dirección de correo electrónico'])-1):
    
    if Eval_18_19_20_21_mod['Dirección de correo electrónico'][i] == (Eval_18_19_20_21_mod
    ['Dirección de correo electrónico'][i + 1]) and Eval_18_19_20_21_mod['Nombre y Apellido'][i] != (
        Eval_18_19_20_21_mod['Nombre y Apellido'][i + 1]):

        Eval_18_19_20_21_mod['Nombre y Apellido'][i + 1] = (
            Eval_18_19_20_21_mod['Nombre y Apellido'][i])

Eval_18_19_20_21_mod.to_csv('Eval_18_19_20_21_mod_1.csv')


# Ahora voy a tratar de modificar el nombre de los cursos

eval_cursos = pd.read_csv('eval_cursos_editado.csv')
eval_cursos.columns.values

for i in range(0, len(Eval_18_19_20_21_mod[
    '¿Cual fue el curso o actividad de Educación Permanente que realizaste?'])):

    for j in range(0, len(eval_cursos['cursos_originales'])):

        if Eval_18_19_20_21_mod[
            '¿Cual fue el curso o actividad de Educación Permanente que realizaste?'][i] == (
            eval_cursos['cursos_originales'][j]):

            Eval_18_19_20_21_mod[
                '¿Cual fue el curso o actividad de Educación Permanente que realizaste?'][i] = (
                eval_cursos['cursos_corregidos'][j])


Eval_18_19_20_21_mod.to_csv('Eval_18_19_20_21_mod_2.csv')
