from fastapi import FastAPI
import numpy as np
import pandas as pd


app = FastAPI()

# http://127.0.0.1:8000 
df = pd.read_csv(('./movies_data/movies_dataset_TandRBylanguage.csv'))


@app.get('/')
def score_titulo(title):

    # Ingresando el título de una filmación, da como respuesta:
    # - Título
    # - Año de estreno
    # - Score.

    row = df[df['title'] == title].index[0]

    score = str(df['vote_average'][row])
    year = str(df['release_year'][row])

    sentence = 'La película \'' + title + '\' fue estrenada en el año ' + year + ' con un score/popularidad de: ' + score
    
    return sentence

"""
@app.get('/votos')
def votos_titulo(title):

    # Ingresando el título de una filmación, devuelve:
    # - 1. Título
    # - 2. Cantidad de votos
    # - 3. Valor promedio de las votaciones
    # La variable (2) deberá de contar con al menos 2000 valoraciones, caso contrario, 
    # avisa que no cumple esta condición y que por ende, no se devuelve ningun valor.

    row = df[df['title'] == title].index[0]

    score = str(df['vote_average'][row])
    year = str(df['release_year'][row])

    voto_count = str(df['vote_count'][row])
    voto_str = 'La misma no tiene el número de votos mínimo para poder informar su votación'

    if voto_count >= 2000:

        voto_str = 'La misma cuenta con un total de ' + voto_count + ' valoraciones, con un promedio de ' + score
       

    sentence = 'La película \'' + title + '\' fue estrenada en el año ' + year + '. ' + voto_str
"""