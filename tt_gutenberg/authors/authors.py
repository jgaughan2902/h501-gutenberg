import pandas as pd

def list_authors(by_languages=True, alias = True):
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    try:
        df = pd.read_csv(url)
    except Exception as e:
        return [f'Error getting data: {e}']
    
    if alias and 'alias' in df.columns and 'translation' in df.columns:
        alias_translation_counts = df.groupby('alias')['translation'].sum()

        sorted_aliases = alias_translation_counts.sort_values(ascending=False)

        return sorted_aliases.index.tolist()
    
    else:
        return []