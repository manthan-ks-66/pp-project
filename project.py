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

# This is a 2D NumPy array (or matrix) where:

# Each row = 1 user

# Each column = 1 song

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
    #  It basically multiplies the corresponding ratings of the two songs and adds them up.
    num = np.dot(a, b)
    # This line calculates the product of the magnitudes (lengths) of the two vectors.

    # It uses np.linalg.norm() which gives the Euclidean length (like the size) of the vector.
    denom = np.linalg.norm(a) * np.linalg.norm(b)

    # Finally, this line calculates the cosine similarity using the formula:
    # If the denominator is 0 (which can happen if one vector is all zeroes), it returns 0 to avoid division by zero.

    return num / denom if denom != 0 else 0

# Recommends top_n most similar songs to the one chosen.
def recommend_similar_songs(song_index, ratings, song_names, top_n=3):
    # Gets ratings column for the selected song (across all users).
    target_song_ratings = ratings[:, song_index]
    similarities = []

    #  This loop is going through each song one by one.

    # len(song_names) is 10 (since we have 10 songs).

    # So i goes from 0 to 9 (index of each song).

    for i in range(len(song_names)):
        # This means: “Skip the song the user already selected.”

        # We don’t want to compare the song to itself.

        # So, if the current song is the same as the one user chose (i == song_index), it skips to the next one.
        if i == song_index:
            continue

        #  This calculates the cosine similarity between:

        #  arget_song_ratings → ratings of the song the user selected.

        #  ratings[:, i] → ratings of the current song in the loop (column i of the ratings matrix).

        # It checks how similar both songs are based on user ratings.
        sim = cosine_similarity(target_song_ratings, ratings[:, i])
        similarities.append((song_names[i], sim))

    # Sorts by similarity score (high to low).
    # Returns top 3 similar songs.
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
        # Calls the recommendation function to get similar songs.
        recommendations = recommend_similar_songs(choice, ratings, song_names)
        # Prints out the top 3 recommended songs with similarity scores.
        print(f"\nBecause you liked '{song_names[choice]}', you might also like:")
        for song, score in recommendations:
            print(f"- {song} (Similarity: {score:.2f})")
    else:
        print("❌ Invalid choice. Please enter a number between 1 and 10.")
except ValueError:
    print("❌ Invalid input. Please enter a number.")

recommended_songs = ["Shape of You", "Stay", "Bad Habits"]
similarity_scores = [0.99, 0.97, 0.96]

plt.bar(recommended_songs, similarity_scores, color='red')
plt.xlabel("Recommended Songs")
plt.ylabel("Similarity Score")
plt.title("Top 3 Similar Songs to 'Blinding Lights'")
plt.ylim(0.9, 1.0)
plt.show()

