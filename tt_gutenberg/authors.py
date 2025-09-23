import pandas as pd
from .utils import fetch_data, sort_aliases_by_translation_count

def list_authors(by_languages=False, alias=False):
    """
    Shows project Gutenberg aliases sorted by translation counts.

    Paramters:
    by_languages (bool): If True, sorts authors by the number 
    of translations.
    alias (bool): If True, will return author aliases instead 
    of main author names.

    Returns:
    A list of author aliases sorted in descending order based
    on translation count.
    """
    # If both arguments/parameters are true, continue.
    if by_languages and alias:

        # The data frame becomes the Gutenberg dataset.
        df = fetch_data()

        # If it isn't None, perform sorting function.
        if df is not None:
            return sort_aliases_by_translation_count(df)
        else:
            return ["Error: Unable to fetch data"]
    
    # Otherwise just return an empty list
    return []