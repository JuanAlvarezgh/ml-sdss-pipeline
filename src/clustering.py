# src/clustering.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from src.utils import cargar_datos, guardar_metricas, ruta_output

def ejecutar_clustering():
    print("\n===== CLUSTERING KMEANS =====")
    df = cargar_datos()
    features = ['u', 'g', 'r', 'i', 'z']
    X = df[features].values
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X)
    le = LabelEncoder()
    clases_reales = le.fit_transform(df['class'])
    print(f"Clusters encontrados: {np.unique(clusters)}")
    print(f"Inercia: {kmeans.inertia_:.2f}")
    metricas = {
        "modelo": "KMeans",
        "n_clusters": 3,
        "inertia": round(float(kmeans.inertia_), 2),
        "features": features,
        "distribucion_clusters": {
            str(k): int(np.sum(clusters == k)) for k in range(3)
        }
    }
    guardar_metricas("metricas_clustering.json", metricas)
    colores = ['#e74c3c', '#2ecc71', '#3498db']
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    for k in range(3):
        mask = clusters == k
        axes[0].scatter(X[mask, 1], X[mask, 2], c=colores[k],
                        label=f'Cluster {k}', alpha=0.6, s=20)
    axes[0].set_xlabel('Magnitud g')
    axes[0].set_ylabel('Magnitud r')
    axes[0].set_title('KMeans — Clusters obtenidos')
    axes[0].legend()
    for idx, clase in enumerate(le.classes_):
        mask = clases_reales == idx
        axes[1].scatter(X[mask, 1], X[mask, 2], c=colores[idx],
                        label=clase, alpha=0.6, s=20)
    axes[1].set_xlabel('Magnitud g')
    axes[1].set_ylabel('Magnitud r')
    axes[1].set_title('Clases reales')
    axes[1].legend()
    plt.suptitle('Clustering KMeans vs Clases Reales', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(ruta_output('clustering_comparacion.png'), dpi=150)
    plt.close()
    print("[OK] Gráfica guardada: clustering_comparacion.png")
    return metricas

if __name__ == "__main__":
    ejecutar_clustering()