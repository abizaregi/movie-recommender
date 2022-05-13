import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_desc = []
    recommended_movie_posters = []
    recommended_movie_genre = []
    for i in distances[1:10]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_desc.append(movies.iloc[i[0]].desc)
        recommended_movie_genre.append(movies.iloc[i[0]].genres)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_desc, recommended_movie_genre

st.title('🎬 Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Please Wait...'):
        recommended_movie_names,recommended_movie_posters, recommended_movie_desc, recommended_movie_genre = recommend(selected_movie)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
            st.caption(recommended_movie_desc[0])
            st.caption(f'Genre: {recommended_movie_genre[0]}')
        with col2:
            st.subheader(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
            st.caption(recommended_movie_desc[1])
            st.caption(f'Genre: {recommended_movie_genre[1]}')
        with col3:
            st.subheader(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
            st.caption(recommended_movie_desc[2])
            st.caption(f'Genre: {recommended_movie_genre[2]}')

        st.write('--------------------------------------')
        col4, col5, col6 = st.columns(3)
        with col4:
            st.subheader(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
            st.caption(recommended_movie_desc[3])
            st.caption(f'Genre: {recommended_movie_genre[3]}')
        with col5:
            st.subheader(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
            st.caption(recommended_movie_desc[4])
            st.caption(f'Genre: {recommended_movie_genre[4]}')
        with col6:
            st.subheader(recommended_movie_names[5])
            st.image(recommended_movie_posters[5])
            st.caption(recommended_movie_desc[5])
            st.caption(f'Genre: {recommended_movie_genre[5]}')
            
        st.write('--------------------------------------')
        col7, col8, col9 = st.columns(3)
        with col7:
            st.subheader(recommended_movie_names[6])
            st.image(recommended_movie_posters[6])
            st.caption(recommended_movie_desc[6])
            st.caption(f'Genre: {recommended_movie_genre[6]}')
        with col8:
            st.subheader(recommended_movie_names[7])
            st.image(recommended_movie_posters[7])
            st.caption(recommended_movie_desc[7])
            st.caption(f'Genre: {recommended_movie_genre[7]}')
        with col9:
            st.subheader(recommended_movie_names[8])
            st.image(recommended_movie_posters[8])
            st.caption(recommended_movie_desc[8])
            st.caption(f'Genre: {recommended_movie_genre[8]}')

    st.success('Enjoy your movies')
    st.snow()

st.code(
    '''
    for you in user_this_app:
        this_app = 'Movie Recommender System'
        this_app.created_by:
            for i in kelompok_18:
                i[0] = 'Abizar Egi Mahendra'
                i[1] = 'Your name'
                i[2] = 'Your name'
                i[3] = 'Your name'
                i[4] = 'Your name'
            print('Final Project for Python DTS KOMINFO')
        return thank_you
    ''', language=python
)








