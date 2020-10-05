import re
from gensim.parsing.preprocessing import remove_stopwords

def file_prep(resume: str) -> str:
    """
    Reads resume string, changes to lowercase and removes special characters.
    
    Parameters
    ----------
    path_to_file : str
        The path to the file
        
    Returns
    -------
    str
    
    Examples
    --------
    
    """
    cleaned_str = re.sub('[^A-Za-z0-9%@.$ ]+', '', resume).lower()

    return cleaned_str

def remove_stop_words(resume_str: str) -> str:
    """
    Reads cleaned resume text and removes stopwords. Used for text analysis.
    
    Stopwords are words like the, in, a, ...

    Parameters
    ----------
    resume_str : str
        The resume parsed as string.
        
    Returns
    -------
    str
    
    Examples
    --------
    
    """
    filtered_resume = remove_stopwords(resume)

    return filtered_resume
