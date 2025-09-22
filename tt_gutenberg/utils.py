import pandas as pd

def fetch_data():
    """
    Fetches the Project Gutenberg author data from a public URL.
    Returns:
        pd.DataFrame: A DataFrame of the author data, or None if fetching fails.
    """
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def sort_aliases_by_translation_count(df):
    """
    Sorts a DataFrame of authors by the number of translations for each alias.
    Args:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        list: A list of author aliases sorted by translation count in descending order.
    """
    aliases_df = df.copy()
    aliases_df['aliases'] = aliases_df['aliases'].fillna(aliases_df['alias']).fillna(aliases_df['author'])
    aliases_df['aliases'] = aliases_df['aliases'].astype(str).str.split('/')
    aliases_df = aliases_df.explode('aliases')
    aliases_df['aliases'] = aliases_df['aliases'].str.strip()
    aliases_df = aliases_df[aliases_df['aliases'].str.contains(r'[a-zA-Z]')]
    translation_counts = aliases_df.groupby('aliases').size().reset_index(name='translation_count')
    sorted_aliases_df = translation_counts.sort_values(by='translation_count', ascending=False)
    return sorted_aliases_df['aliases'].tolist()