
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
from src.utils import cargar_datos, guardar_metricas, ruta_output

def ejecutar_clasificacion():
    print("\n===== CLASIFICACIÓN KNN =====")
    df = cargar_datos()
    features = ['u', 'g', 'r', 'i', 'z', 'redshift']
    X = df[features].values
    le = LabelEncoder()
    y = le.fit_transform(df['class'])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    print(f"Entrenamiento: {X_train.shape[0]} muestras | Prueba: {X_test.shape[0]} muestras")
    modelo = KNeighborsClassifier(n_neighbors=5)
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    reporte = classification_report(y_test, y_pred, target_names=le.classes_)
    print(f"Accuracy: {accuracy:.4f}")
    print("\nMatriz de Confusión:")
    print(cm)
    print("\nReporte de Clasificación:")
    print(reporte)
    metricas = {
        "modelo": "KNN",
        "k": 5,
        "division": "70/30",
        "accuracy": round(float(accuracy), 4),
        "matriz_confusion": cm.tolist(),
        "clases": list(le.classes_)
    }
    guardar_metricas("metricas_clasificacion.json", metricas)
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=le.classes_, yticklabels=le.classes_, ax=ax)
    ax.set_title('Matriz de Confusión — KNN (k=5)', fontsize=14)
    ax.set_xlabel('Predicho')
    ax.set_ylabel('Real')
    plt.tight_layout()
    plt.savefig(ruta_output('clasificacion_confusion_matrix.png'), dpi=150)
    plt.close()
    print("[OK] Gráfica guardada: clasificacion_confusion_matrix.png")
    return metricas

if __name__ == "__main__":
    ejecutar_clasificacion()