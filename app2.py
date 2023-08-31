import streamlit as st
import pickle
import pandas as pd
import requests
import json
def fetch_poster(movie_id):
    

    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c00acefa944091fd1d869efdb2f250e3'.format(movie_id))

# print(response.text)
#     response = requests.get('https://api.themoviedb.org/3/search/movie?query={}&include_adult=false&language=en-US&page=1'.format(movie_id))
    data= json.loads(response.text)
    st.text(data)
    return 'https://image.tmdb.org/t/p/w92/' + data['poster_path']




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies_list=[]
    recommended_movies_posters=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_list.append((movies.iloc[i[0]].title))
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_list,recommended_movies_posters


 
movies_dict = pickle.load(open('D:\OneDrive\Desktop\python\moviersystem\movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('D:\OneDrive\Desktop\python\moviersystem\similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Enter a Movie Name',
    movies["title"].values)

if st.button('Recommend'):
    
    
    
    names,posters = recommend(selected_movie_name)
    for i in names:
        st.text(i)
    # col1, col2, col3, col4, col5 = st.columns(5)

    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])

    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])

    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])

    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])

    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
        