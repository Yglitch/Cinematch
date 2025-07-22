import streamlit as st
import pandas as pd

# -------------------- Load Data --------------------
st.set_page_config(page_title="CineMatch 🎬", layout="centered")
st.title("🎥 CineMatch")

@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")  # movieId, title, genres
    ratings = pd.read_csv("ratings.csv")  # userId, movieId, rating
    return movies, ratings

movies_df, ratings_df = load_data()

# -------------------- Prepare Data --------------------
# Merge ratings with movies
merged_df = pd.merge(ratings_df, movies_df, on="movieId")

# Calculate average rating & count
movie_stats = merged_df.groupby(['movieId', 'title', 'genres']).agg(
    avg_rating=('rating', 'mean'),
    rating_count=('rating', 'count')
).reset_index()

# Optional: Only show movies with at least X ratings
movie_stats = movie_stats[movie_stats['rating_count'] >= 20]

# -------------------- Genre Filter --------------------
genre_list = sorted(set(
    genre
    for sublist in movies_df['genres'].fillna('').str.split('|')
    for genre in sublist if genre
))
selected_genre = st.selectbox("Filter by Genre (optional):", ["All"] + genre_list)

if selected_genre != "All":
    movie_stats = movie_stats[movie_stats['genres'].str.contains(selected_genre, na=False)]

# -------------------- Top Recommendations --------------------
top_n = st.slider("How many recommendations do you want?", 5, 20, 10)

st.subheader(f"🎯 Top {top_n} Most Loved Movies:")

top_movies = movie_stats.sort_values(by='avg_rating', ascending=False).head(top_n)

for _, row in top_movies.iterrows():
    st.markdown(f"**🎬 {row['title']}**")
    st.markdown(f"Genres: *{row['genres']}*")
    st.markdown(f"⭐ Average Rating: {row['avg_rating']:.2f} ({int(row['rating_count'])} ratings)")
    st.markdown("---")
