# 🎬 CineMatch

**CineMatch** is a movie recommendation system that suggests films based on user preferences or overall popularity. Built with Python, Surprise (for collaborative filtering), and Streamlit for an interactive web UI, it allows users to explore movies filtered by genre and rating.

---

## 🚀 Features

- 📈 **Personalized Recommendations** using SVD (collaborative filtering)
- 🎭 **Genre-Based Filtering** to narrow down suggestions
- ⭐ **Popularity-Based Suggestions** for new or anonymous users
- 🎥 **Real Movie Dataset** from public sources (e.g., MovieLens)
- 📊 **Interactive UI** built using Streamlit

---

## 📁 Project Structure

cinematch/
├── movies.csv # Movie metadata (movieId, title, genres)

├── ratings.csv # User ratings (userId, movieId, rating)

├── svd_model.pkl # Pre-trained SVD model (optional for personalization)

├── app.py # Main Streamlit application

├── requirements.txt # Project dependencies

└── README.md # You're here!


---

## 🧠 How It Works

- **Collaborative Filtering (SVD)**: Learns user preferences from past ratings to recommend new movies.
- **Genre Filter**: User can choose to view only recommendations in a specific genre (e.g., Action, Drama).
- **Unseen Movie Filtering**: Only movies the user hasn’t rated are recommended.
- **Popularity Mode** (optional version): Recommends based on highest average rating with enough votes.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cinematch.git
cd cinematch


2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4.Run the App

streamlit run app.py


🙌 Author
Made with ❤️ by [Yash Rana]
GitHub: @Yglitch
