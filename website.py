import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_tags.pkl", "rb"))

list_of_all_titles = movies["title"].values

st.header("Movie Recommandation System")

similarity = pickle.load(open("similarity.pkl", "rb"))

select = st.selectbox("Select the movies name from drop down and You can also write: ", list_of_all_titles)

def fetch_poster(movies_id):
    url = f"https://api.themoviedb.org/3/movie/{movies_id}?api_key=bf1bac086906bebbc0030828a2969eb1"
    data = requests.get(url).json()
    #data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):

    index_of_movie = movies[movies.title==movie].index[0]

    similarity_score = list(enumerate(similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_score, reverse=True, key = lambda vector:vector[1])

    recommand_movies=[]
    recommend_poster = []
    for i in sorted_similar_movies[:10]:
        movies_id = movies.iloc[i[0]].id
        recommand_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommand_movies, recommend_poster    

if st.button("Show movies"):
    movie_names, movies_poster = recommend(select)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_names[0])      
        st.image(movies_poster[0])
        
    with col2:
        st.text(movie_names[1])
        st.image(movies_poster[1])
            
    with col3:
        st.text(movie_names[2])
        st.image(movies_poster[2])
           
    with col4:
        st.text(movie_names[3])    
        st.image(movies_poster[3])
    with col5:
        st.text(movie_names[4])
        st.image(movies_poster[4])   
    with col5:
        st.text(movie_names[5])
        st.image(movies_poster[5])    
    with col1:
        st.text(movie_names[6])      
        st.image(movies_poster[6])
        
    with col2:
        st.text(movie_names[7])
        st.image(movies_poster[7])
            
    with col3:
        st.text(movie_names[8])
        st.image(movies_poster[8])
           
    with col4:
        st.text(movie_names[9])    
        st.image(movies_poster[9])
  