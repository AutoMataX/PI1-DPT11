from fastapi import FastAPI
import numpy as np
import pandas as pd


app = FastAPI()

# http://127.0.0.1:8000 


#Auxiliary structures:

dict_month = {'Enero':'1', 'Febrero':'2', 'Marzo':'3', 'Abril':'4', 'Mayo':'5', 'Junio':'6',
        'Julio':'7', 'Agosto':'8', 'Septiembre':'9', 'Octubre':'10', 'Noviembre': '11', 'Diciembre':'12'}

dict_day = {'Lunes':'0', 'Martes':'1', 'Miercoles':'3',
              'Jueves':'4', 'Friday':'5', 'Sabado':'6', 'Domingo':'7'}

df = pd.read_csv('./movies_data/movies_dataset.csv')


@app.get('/', debug = True)
def score_titulo(titulo):

    # Ingresando el título de una filmación, da como respuesta:
    # - Título
    # - Año de estreno
    # - Score.

    #row = df[df['title'] == titulo].index[0]
    row = df.index[df['title'] == titulo][0]

    score = str(df['vote_average'][row])
    year = str(df['release_year'][row])

    sentence = 'La película \'' + titulo + '\' fue estrenada en el año ' + year + ' con un score/popularidad de: ' + score
    # (f"La pelicula {titulo}, fue estrenada en el año {year}, con un score/popularidad de: {score}")

    return sentence


@app.get('/votos', debug = True)
def votos_titulo(titulo):

    # Ingresando el título de una filmación, devuelve:
    # - 1. Título
    # - 2. Cantidad de votos
    # - 3. Valor promedio de las votaciones
    # La variable (2) deberá de contar con al menos 2000 valoraciones, caso contrario, 
    # avisa que no cumple esta condición y que por ende, no se devuelve ningun valor.

    row = df.index[df['title'] == titulo][0]

    score = str(df['vote_average'][row])
    year = str(df['release_year'][row])

    voto_count = df['vote_count'][row]
    voto_str = 'La misma no tiene el número de votos mínimo para poder informar su votación'

    if voto_count >= 2000:

        voto_str = 'La misma cuenta con un total de ' + str(voto_count) + ' valoraciones, con un promedio de ' + score
       

    sentence = 'La película \'' + titulo + '\' fue estrenada en el año ' + year + '. ' + voto_str

    return sentence



@app.get('/cantidad mes', debug = True)
def cantidad_filmaciones_mes(mes): 

    # Se ingresa un mes en idioma Español. Devuelve: 
    # - Cantidad de películas estrenadas en el mes consultado, en la TOTALIDAD del dataset
    # It uses a dictionary created on the first sections of this script: 'dict_mont'

    amount = np.shape(df[df['release_month'].astype(str) == dict_month[mes]])[0]

    sentence = 'La cantidad de películas fueron estrenadas en el mes de ' + mes + ' fueron: ' + str(amount)

    return sentence



@app.get('/cantidad dia', debug = True)
def cantidad_filmaciones_dia(dia): 

    # Se ingresa un dia en idioma Español. Devuelve: 
    # - Cantidad de películas estrenadas en el dia consultado, en la TOTALIDAD del dataset
    # It uses a dictionary created on the first sections of this script: 'dict_dia'

    amount = np.shape(df[df['release_day'].astype(str) == dict_day[dia]])[0]

    sentence = 'La cantidad de películas fueron estrenadas en el dia ' + dia + ' fueron: ' + str(amount)

    return sentence





### RECOMENDATION SYSTEM

@app.get('/recomendacion', debug = True)
def recomendacion(titulo):

    # This function recommend 5 movies based on a movie that you already like

    #Getting sample parameteres:
    row = df.index[df['title'] == titulo][0] 
    sub_df = df[df['genres'] == df['genres'].iloc[row]]
    sub_df = sub_df[['title', 'genres', 'vote_average', 'popularity']]

    recommended_movies = sub_df[sub_df['title'] != titulo].sort_values(by = ['popularity', 'vote_average'], ascending = False)['title'].head(5)

    recommended_movies = '/ '.join(recommended_movies)

    #sentence = 'Basado en la película ingresada, le recomendamos los siguientes títulos: ' + recommended_movies

    return (f"Basado en la pelicula ingresada, le recomendamos los siguientes titulos: {recommended_movies}")





