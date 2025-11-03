import pandas as pd
import numpy as np

df_tests = pd.read_csv("./data/dataset/dgt_driving_schools_tests.csv")
df_tests = df_tests[df_tests["provincia"] == "Palmas (Las)"]
df_driving_schools = pd.read_csv("./data/dataset/driving_schools_information.csv")
df_final = pd.merge(
    df_driving_schools,
    df_tests,
    on="codigo_centro",
    how="left",
    suffixes=('', '_y')  # las columnas repetidas del derecho tendrán _y
)

# Eliminar columnas del derecho
df_final = df_final.loc[:, ~df_final.columns.str.endswith('_y')]
df_final.to_csv("dataset.csv")
