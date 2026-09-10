import pandas as pd
from difflib import get_close_matches


def load_dataset(path="bhutia_data.csv"):
    return pd.read_csv(path)


def search_word(query, df, n=3, cutoff=0.6):
    query = query.strip().lower()
    search_pool = []
    for i, row in df.iterrows():
        search_pool.append((str(row['english']).lower(), i))
        search_pool.append((str(row['nepali']).lower(), i))
    words = [w for w, i in search_pool]
    matches = get_close_matches(query, words, n=n, cutoff=cutoff)
    results = []
    for m in matches:
        idx = [i for w, i in search_pool if w == m][0]
        results.append(df.iloc[idx])
    return results


def log_missing_word(word, path="logs/wishlist.txt"):
    import os
    os.makedirs("logs", exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(word + "\n")