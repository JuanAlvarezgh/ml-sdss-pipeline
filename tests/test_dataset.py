# tests/test_dataset.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
import pytest
from src.utils import cargar_datos, DATA_PATH

def test_archivo_existe():
    assert os.path.exists(DATA_PATH)

def test_columnas_correctas():
    df = cargar_datos()
    for col in ['u', 'g', 'r', 'i', 'z', 'redshift', 'class']:
        assert col in df.columns

def test_sin_valores_nulos():
    df = cargar_datos()
    assert df[['u', 'g', 'r', 'i', 'z', 'redshift', 'class']].isnull().sum().sum() == 0

def test_clases_correctas():
    df = cargar_datos()
    assert set(df['class'].unique()) == {'Galaxy', 'Star', 'QSO'}

def test_numero_minimo_filas():
    df = cargar_datos()
    assert len(df) >= 100

def test_valores_numericos():
    df = cargar_datos()
    for col in ['u', 'g', 'r', 'i', 'z', 'redshift']:
        assert pd.api.types.is_numeric_dtype(df[col])