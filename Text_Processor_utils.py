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
    
#We can also read the text data from the local machine
def read_local_text_data(file_path):
    """
    Reads the contents of a text file from a local path.

    Args:
    ----------
    file_path : str
        The path to the text file on the local machine.

    Returns:
    -------
    str
        The full text content of the file as a string.

    Raises:
    ------
    FileNotFoundError
        If the specified file path does not exist.
    IOError
        If there is an error reading the file.
    """
    with open(file_path, 'r', encoding= 'utf-8') as file:
        text_data = file.read()
    return text_data

def remove_punctuations(words):
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
    words  = words.lower()
    return ''.join([word for word in words if word not in string.punctuation])

def bag_of_words_count(words:list, word_dict= {}):
    """
    Counts the occurrences of each word in a given list and returns a dictionary 
    with the word counts.

    Args
    ----------
    words : list
        A list of words to count.
    word_dict : dict, optional
        An existing dictionary to update with word counts (default is an empty dictionary).

    Returns
    -------
    dict
        A dictionary where keys are words and values are their corresponding counts.
    """
    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word]= 1
    return word_dict

    
