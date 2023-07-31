import streamlit as st
import pickle
import requests



def fetch_poster(movie_id):

    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=9c02d93df061274070d7e53a2da64202&language=en-US')
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):

    movie_index = movies_data[movies_data['title'] == movie].index[0]
    movie_distance=corr.iloc[movie_index].values
    movie_list=sorted(list(enumerate(movie_distance)) , reverse=True , key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_poster=[]
    for i in movie_list:
        movie_id = movies_data.iloc[i[0], 0]
        recommend_movies.append(movies_data.iloc[i[0]].title)
        #fetch poster using API
        recommend_poster.append(fetch_poster(movie_id))


    return recommend_movies,recommend_poster


movies_data = pickle.load(open('movies.pkl','rb'))
corr = pickle.load(open('corr.pkl','rb'))



st.title('Movie Recommendation System')

selected_movie = st.selectbox('Enter Movie Name',(movies_data['title'].values))

if st.button('RECOMMEND'):

    names,poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])