# utils/data_loader.py
import pandas as pd

def load_dataset(path='data/dataset.csv'): 
    # Load the dataset path by copying the path of the specific dataset from the data folder and pasting it here
    df = pd.read_csv(path)
    return df

def load_severity(path='data/Symptom-severity.csv'):
    return pd.read_csv(path)

def get_symptom_columns(df):
    return [col for col in df.columns if col.startswith('Symptom')]

def build_graph(df):
    symptom_cols = get_symptom_columns(df)
    graph = {}
    for _, row in df.iterrows():
        symptoms = [row[col] for col in symptom_cols if pd.notna(row[col])]
        for s in symptoms:
            if s not in graph:
                graph[s] = set()
            for other in symptoms:
                if other != s:
                    graph[s].add(other)
    return {k: list(v) for k, v in graph.items()}