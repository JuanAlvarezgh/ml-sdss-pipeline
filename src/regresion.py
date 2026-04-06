# src/regresion.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from src.utils import cargar_datos, guardar_metricas, ruta_output

def ejecutar_regresion():
    print("\n===== REGRESIÓN LINEAL =====")
    df = cargar_datos()
    features = ['u', 'g', 'r', 'i', 'z']
    X = df[features].values
    y = df['redshift'].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    print(f"Entrenamiento: {X_train.shape[0]} muestras | Prueba: {X_test.shape[0]} muestras")
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MSE:  {mse:.4f}")
    print(f"R²:   {r2:.4f}")
    metricas = {
        "modelo": "Regresión Lineal",
        "variable_objetivo": "redshift",
        "features": features,
        "MSE": round(float(mse), 4),
        "R2": round(float(r2), 4)
    }
    guardar_metricas("metricas_regresion.json", metricas)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(y_test, y_pred, alpha=0.5, color='steelblue', edgecolors='k', linewidths=0.3)
    lim_min = min(y_test.min(), y_pred.min())
    lim_max = max(y_test.max(), y_pred.max())
    ax.plot([lim_min, lim_max], [lim_min, lim_max], 'r--', linewidth=1.5, label='Predicción perfecta')
    ax.set_xlabel('Redshift Real')
    ax.set_ylabel('Redshift Predicho')
    ax.set_title(f'Regresión Lineal — Real vs Predicho\nMSE={mse:.4f} | R²={r2:.4f}', fontsize=12)
    ax.legend()
    plt.tight_layout()
    plt.savefig(ruta_output('regresion_real_vs_predicho.png'), dpi=150)
    plt.close()
    print("[OK] Gráfica guardada: regresion_real_vs_predicho.png")
    return metricas

if __name__ == "__main__":
    ejecutar_regresion()