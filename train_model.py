from surprise import SVD, Dataset, Reader
import pandas as pd
import joblib

ratings_df = pd.read_csv("ratings.csv")
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)
trainset = data.build_full_trainset()

model = SVD()
model.fit(trainset)
joblib.dump(model, "svd_model.pkl")
