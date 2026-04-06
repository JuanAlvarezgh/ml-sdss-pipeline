import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.clasificacion import ejecutar_clasificacion
from src.regresion import ejecutar_regresion
from src.clustering import ejecutar_clustering

def main():
    print("=" * 50)
    print("  PIPELINE ML — DATOS ASTRONÓMICOS SDSS")
    print("=" * 50)
    resultados = {}
    resultados['clasificacion'] = ejecutar_clasificacion()
    resultados['regresion'] = ejecutar_regresion()
    resultados['clustering'] = ejecutar_clustering()
    print("\n" + "=" * 50)
    print("  RESUMEN DE MÉTRICAS")           
    print("=" * 50)
    print(f"  KNN Accuracy:     {resultados['clasificacion']['accuracy']:.4f}")
    print(f"  Regresión MSE:    {resultados['regresion']['MSE']:.4f}")
    print(f"  Regresión R²:     {resultados['regresion']['R2']:.4f}")
    print(f"  KMeans Inertia:   {resultados['clustering']['inertia']:.2f}")
    print("=" * 50)
    print("\n[COMPLETADO] Revisa la carpeta outputs/")

if __name__ == "__main__":
    main()