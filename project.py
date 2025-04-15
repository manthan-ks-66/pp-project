import numpy as np
import matplotlib.pyplot as plt


# Song list (dataset)
song_names = [
    "Blinding Lights - The Weeknd",
    "Shape of You - Ed Sheeran",
    "Someone You Loved - Lewis Capaldi",
    "Levitating - Dua Lipa",
    "Bad Habits - Ed Sheeran",
    "Stay - The Kid LAROI & Justin Bieber",
    "Peaches - Justin Bieber",
    "As It Was - Harry Styles",
    "Senorita - Shawn Mendes & Camila Cabello",
    "Watermelon Sugar - Harry Styles"
]

# Simulated user ratings (6 users x 10 songs)
ratings = np.array([
    [5, 4, 3, 5, 4, 5, 2, 3, 4, 4],
    [4, 5, 4, 4, 5, 5, 3, 3, 4, 3],
    [1, 2, 5, 1, 1, 2, 5, 4, 2, 2],
    [5, 5, 3, 4, 5, 5, 4, 3, 5, 4],
    [2, 1, 5, 1, 1, 2, 4, 5, 1, 2],
    [4, 4, 2, 5, 4, 4, 3, 2, 4, 3]
])

def cosine_similarity(a, b):
    num = np.dot(a, b)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return num / denom if denom != 0 else 0

def recommend_similar_songs(song_index, ratings, song_names, top_n=3):
    target_song_ratings = ratings[:, song_index]
    similarities = []

    for i in range(len(song_names)):
        if i == song_index:
            continue
        sim = cosine_similarity(target_song_ratings, ratings[:, i])
        similarities.append((song_names[i], sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_n]

# Display the song choices
print("🎵 Available Songs:")
for idx, song in enumerate(song_names):
    print(f"{idx + 1}. {song}")

# Taking user input
try:
    choice = int(input("\nEnter the number of a song you like (1-10): ")) - 1
    if 0 <= choice < len(song_names):
        recommendations = recommend_similar_songs(choice, ratings, song_names)
        print(f"\nBecause you liked '{song_names[choice]}', you might also like:")
        for song, score in recommendations:
            print(f"- {song} (Similarity: {score:.2f})")
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 10.")
except ValueError:
    print("❌ Invalid input. Please enter a number.")

recommended_songs = ["Shape of You", "Stay", "Bad Habits"]
similarity_scores = [0.99, 0.97, 0.96]

plt.bar(recommended_songs, similarity_scores, color='skyblue')
plt.xlabel("Recommended Songs")
plt.ylabel("Similarity Score")
plt.title("Top 3 Similar Songs to 'Blinding Lights'")
plt.ylim(0.9, 1.0)
plt.show()

