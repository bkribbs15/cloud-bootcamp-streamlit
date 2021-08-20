import streamlit as st
import pandas as pd
import os

from recommender_app.config import RESOURCES_FOLDER


def render():
    movies_df = pd.read_csv(os.path.join(RESOURCES_FOLDER, 'movies.csv'), skiprows=1, index_col=0, sep='\t', names=['movie_id', 'title', 'genres'])

    movie_list = movies_df['title']

    st.title('Movie recommender app')

    form = st.form(key='my-form')

    form.markdown('Please choose three movies from the list below')

    movie1 = form.selectbox(
        'Movie 1', 
        [
            'Select one option', 
            *movie_list
        ]
    )

    movie2 = form.selectbox(
        'Movie 2', 
        [
            'Select one option', 
            *movie_list
        ]
    )

    movie3 = form.selectbox(
        'Movie 3', 
        [
            'Select one option', 
            *movie_list
        ]
    )


    submit = form.form_submit_button('Submit')

    if  submit:

        if 'Select one option' in [movie1, movie2, movie3]:
            st.write('Plase choose three movies')
        else:
            st.write(f'hello {name}')
