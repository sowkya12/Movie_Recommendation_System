import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MovieRecommender:
    def __init__(self, movie_data_path):
        # Read CSV with proper quote handling
        self.movies = pd.read_csv(movie_data_path, quotechar='"')
        
        # Create TF-IDF vectorizer
        self.tfidf = TfidfVectorizer(stop_words='english')
        
        # Replace NaN with empty string
        self.movies['description'] = self.movies['description'].fillna('')
        
        # Construct TF-IDF matrix
        self.tfidf_matrix = self.tfidf.fit_transform(self.movies['description'])
        
        # Compute cosine similarity matrix
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
    
    def get_recommendations(self, title, num_recommendations=5):
        # Get the index of the movie that matches the title
        idx = self.movies[self.movies['title'] == title].index[0]
        
        # Get the pairwise similarity scores
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # Sort the movies based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get the scores of the top-n most similar movies
        sim_scores = sim_scores[1:num_recommendations+1]
        
        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]
        
        # Return the top-n most similar movies
        return self.movies['title'].iloc[movie_indices]
