"""
This module contains utility functions for text preprocessing.
It includes functions to perform tasks like removing punctuations.
Dependencies:
    - string (standard Python library)
Usage:
    import string
    from text_utils import remove_punctuations
    text = "Hello, World!"
    cleaned_text = remove_punctuations(text)
    print(cleaned_text)  # Output: Hello World
"""
import string
import urllib
import urllib.request
from nltk.tokenize import TreebankWordDetokenizer

def read_online_text_data(text_url):
    """
    Reads text data from an online resource.
    
    Args:
        url (str): The URL linking to the text data.
    Returns:
        str: The content of the text data as a string.
    """
    with urllib.request.urlopen(url = text_url) as f:
        return f.read().decode('ISO-8859-1')

def remove_punctuations(col):
    """
    Remove all punctuation characters from the input string.
    Args:
        col (str): A string from which punctuation characters should be removed.
    Returns:
        str: A string with all punctuation characters removed.
    Example:
        >>> remove_punctuations("Hello, World!")
        'Hello World'
    """
    return ''.join(words for words in col if words not in string.punctuation)

    
