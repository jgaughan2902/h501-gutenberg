import pandas as pd
from .utils import fetch_data, sort_aliases_by_translation_count

def list_authors(by_languages=False, alias=False):
    """
    Lists Project Gutenberg author aliases in order of translation count.

    Args:
        by_languages (bool): If True, sorts authors by the number of translations.
        alias (bool): If True, returns author aliases instead of main author names.

    Returns:
        list: A list of author aliases sorted by translation count in descending order.
    """
    if by_languages and alias:
        df = fetch_data()
        if df is not None:
            return sort_aliases_by_translation_count(df)
        else:
            return ["Error: Unable to fetch data"]
    
    return []