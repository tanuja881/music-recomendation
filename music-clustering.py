import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go

# Load dataset
data = pd.read_csv("Spotify-2000.csv")

# Features for clustering
features = ["Beats Per Minute (BPM)", "Loudness (dB)", "Liveness", "Valence", 
            "Acousticness", "Speechiness", "Energy", "Danceability"]

# Scale the features
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data[features])

# KMeans clustering
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(data_scaled)
data["Music Segments"] = clusters

# Recommendation function using cosine similarity
def recommend_similar_songs(row_index, num_recommendations=5):
    if row_index >= len(data):
        print("Invalid row index!")
        return
    similarities = cosine_similarity([data_scaled[row_index]], data_scaled)
    similar_indices = similarities.argsort()[0][::-1][1:num_recommendations+1]
    print(f"Recommendations for song at row {row_index}:")
    print(data.iloc[similar_indices][["Year"] + features + ["Music Segments"]])

# Example recommendation
recommend_similar_songs(1)

# 3D Visualization
PLOT = go.Figure()
for i in sorted(data["Music Segments"].unique()):
    PLOT.add_trace(go.Scatter3d(
        x=data[data["Music Segments"] == i]['Beats Per Minute (BPM)'],
        y=data[data["Music Segments"] == i]['Energy'],
        z=data[data["Music Segments"] == i]['Danceability'],                        
        mode='markers',
        marker=dict(size=6, line=dict(width=1)),
        name=f"Cluster {i}"
    ))

PLOT.update_traces(hovertemplate='BPM: %{x} <br>Energy: %{y} <br>Danceability: %{z}')
PLOT.update_layout(
    width=800, height=800, autosize=True, showlegend=True,
    scene=dict(
        xaxis=dict(title='BPM'),
        yaxis=dict(title='Energy'),
        zaxis=dict(title='Danceability')
    )
)
PLOT.show()
