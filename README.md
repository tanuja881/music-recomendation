# 🎵 Spotify Music Clustering & Recommendation System

A project that **analyzes, clusters, and recommends songs** from a Spotify dataset using **KMeans clustering** and **cosine similarity**. It also includes an **interactive 3D visualization** of music clusters.  

---

## ✨ Features

- **Clustering**: Groups songs into **10 clusters** using KMeans based on audio features.  
- **Recommendation**: Suggests **similar songs** using cosine similarity.  
- **Visualization**: Interactive **3D scatter plot** of clusters using `Plotly`.  

---

## 📂 Dataset

The dataset used is `Spotify-2000.csv` and contains songs with the following audio features:

| Feature | Description |
|---------|-------------|
| BPM | Beats Per Minute |
| Loudness | Loudness in dB |
| Liveness | Probability that the track is live |
| Valence | Musical positiveness (0–1) |
| Acousticness | Likelihood of being acoustic |
| Speechiness | Presence of spoken words |
| Energy | Energy of the track (0–1) |
| Danceability | Suitability for dancing |
| Year | Year of release |

> Ensure the dataset is in the same directory as the script or update the file path in the code.

---

