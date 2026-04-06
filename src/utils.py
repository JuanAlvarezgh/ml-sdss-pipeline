# src/utils.py
import pandas as pd
import os
import json

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sdss_sample.csv')
OUTPUTS_PATH = os.path.join(os.path.dirname(__file__), '..', 'outputs')

def cargar_datos():
    df = pd.read_csv(DATA_PATH)
    return df

def guardar_metricas(nombre_archivo, metricas_dict):
    os.makedirs(OUTPUTS_PATH, exist_ok=True)
    ruta = os.path.join(OUTPUTS_PATH, nombre_archivo)
    with open(ruta, 'w') as f:
        json.dump(metricas_dict, f, indent=4)
    print(f"[OK] Métricas guardadas en: {ruta}")

def ruta_output(nombre_archivo):
    os.makedirs(OUTPUTS_PATH, exist_ok=True)
    return os.path.join(OUTPUTS_PATH, nombre_archivo)