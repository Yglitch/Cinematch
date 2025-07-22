import streamlit as st
import pandas as pd
import joblib
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

# -------------------- Load & Prepare --------------------
st.set_page_config(page_title="CineMatch 🎬", layout="centered")
st.title("🎥 CineMatch")

@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")  # movieId, title, genres
    ratings = pd.read_csv("ratings.csv")  # userId, movieId, rating
    return movies, ratings

@st.cache_resource
def load_model():
    return joblib.load("svd_model.pkl")

movies_df, ratings_df = load_data()
model = load_model()

# -------------------- User Input --------------------
user_id = st.number_input("Enter your User ID:", min_value=1, max_value=ratings_df['userId'].max(), step=1)

# Optional Genre Filter

genre_list = sorted(set(
    genre
    for sublist in movies_df['genres'].fillna('').str.split('|')
    for genre in sublist if genre
))
selected_genre = st.selectbox("Filter by Genre (optional):", ["All"] + genre_list)

# -------------------- Recommendation Logic --------------------
def get_unseen_movies(user_id, all_movie_ids, ratings_df):
    rated = ratings_df[ratings_df['userId'] == user_id]['movieId'].tolist()
    return [mid for mid in all_movie_ids if mid not in rated]

def recommend_movies(user_id, model, unseen_movies, top_n=10):
    predictions = [(mid, model.predict(user_id, mid).est) for mid in unseen_movies]
    return sorted(predictions, key=lambda x: x[1], reverse=True)[:top_n]

# -------------------- Recommend Button --------------------
if st.button("Get Recommendations"):
    with st.spinner("Fetching your recommendations..."):
        all_movie_ids = movies_df['movieId'].unique()
        unseen = get_unseen_movies(user_id, all_movie_ids, ratings_df)
        top_recs = recommend_movies(user_id, model, unseen, top_n=10)

        top_movie_ids = [mid for mid, _ in top_recs]
        recommended_df = movies_df[movies_df['movieId'].isin(top_movie_ids)]

        # Add estimated ratings
        estimated_ratings = dict(top_recs)
        recommended_df['Estimated Rating'] = recommended_df['movieId'].map(estimated_ratings)

        # Optional genre filter
        if selected_genre != "All":
            recommended_df = recommended_df[recommended_df['genres'].str.contains(selected_genre)]

        if recommended_df.empty:
            st.warning("No recommendations found for this genre.")
        else:
            st.subheader("🎯 Top Movie Recommendations:")
            for _, row in recommended_df.iterrows():
                st.markdown(f"**🎬 {row['title']}**")
                st.markdown(f"Genres: *{row['genres']}*")
                st.markdown(f"⭐ Estimated Rating: {row['Estimated Rating']:.2f}")
                st.markdown("---")

invalid_genres = movies_df[~movies_df['genres'].apply(lambda x: isinstance(x, str))]
print(invalid_genres)