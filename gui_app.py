import tkinter as tk
from tkinter import messagebox
from recommender import MovieRecommender

class MovieApp:
    def __init__(self, master):
        self.master = master
        master.title("Movie Recommender")
        
        # Initialize recommender with proper CSV handling
        self.recommender = MovieRecommender("movies.csv")
        
        # GUI Elements
        self.label = tk.Label(master, text="Enter a movie title:")
        self.label.pack()
        
        self.entry = tk.Entry(master, width=50)
        self.entry.pack()
        
        self.recommend_button = tk.Button(master, text="Get Recommendations", command=self.get_recommendations)
        self.recommend_button.pack()
        
        self.result_label = tk.Label(master, text="", wraplength=300)
        self.result_label.pack()
    
    def get_recommendations(self):
        title = self.entry.get()
        try:
            recommendations = self.recommender.get_recommendations(title)
            self.result_label.config(text=f"Recommendations for {title}:\n" + "\n".join(recommendations))
        except IndexError:
            messagebox.showerror("Error", "Movie not found in database")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
