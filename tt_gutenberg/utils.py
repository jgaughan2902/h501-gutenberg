import pandas as pd

def fetch_data():
    """
    Gets the project Gutenberg data from the url

    Parameters:
    There are no input paramters
    
    Returns:
    A pd.DataFrame of author data or nothing 
    if there is an error.
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
    Sorts the dataframe of authors by the number of translations
    for each alias.

    Parameters:
    df (pd.DataFrame): The data frame defined from the
    fetch_data() function

    Returns:
    A list of author aliases sorted by number of 
    translations in descending order.
    """
    # Produce a copy of the dataset.
    aliases_df = df.copy()

    # Manage NA values in alias.
    aliases_df['aliases'] = aliases_df['aliases'].fillna(aliases_df['alias']).fillna(aliases_df['author'])

    # Coerce to a string and split.
    aliases_df['aliases'] = aliases_df['aliases'].astype(str).str.split('/')
    
    # Break string into array.
    aliases_df = aliases_df.explode('aliases')

    # Remove leading and trailing whitespace characters.
    aliases_df['aliases'] = aliases_df['aliases'].str.strip()

    # Check for alphabetic characters.
    aliases_df = aliases_df[aliases_df['aliases'].str.contains(r'[a-zA-Z]')]

    # Find number of translation counts
    translation_counts = aliases_df.groupby('aliases').size().reset_index(name='translation_count')

    # Create a df sorted by translation counts.
    sorted_aliases_df = translation_counts.sort_values(by='translation_count', ascending=False)

    # return a list of the sorted aliases column.
    return sorted_aliases_df['aliases'].tolist()