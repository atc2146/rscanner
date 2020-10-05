from typing import Tuple
from collections import Counter
import re

def get_length_of_resume(resume_str: str) -> Tuple[str, str]:
    """
    Returns the number of characters and words in a resume, in that order.

    Parameters
    ----------
    resume_str : str
        The resume parsed as string.
        
    Returns
    -------
    Tuple
    (str, str)	
    """
    try:
        # simple split on whitespace
        num_of_words = len(resume_str.split())
        return len(resume_str), num_of_words
    except:
        raise TypeError('You did not enter a string.')

def resume_length_checker(resume_words: int) -> str:
    """
    Returns an evaluation of the resume's length.

    Parameters
    ----------
    resume_words : int
        The number of words in the resume.
        
    Returns
    -------
    str	
    """
    if (resume_words >= 0 and resume_words <= 325):
        return 'on the shorter side'
    elif (resume_words > 325 and resume_words <= 650):
        return 'optimal'
    else:
        return 'on the longer side'

def count_quantifiable_metrics(resume_str: str) -> str:
    """
    Counts the number of quantifiable metrics in the resume.  Based on string matches of
    keywords such as percent, %, $, dollars, USD, etc.

    Parameters
    ----------
    resume_str :  str
        The resume parsed as string.
        
    Returns
    -------
    str	
    """
    # This can be optimized

    # resume_str = '''This is a test test test string is $100 and percent 200%'''
    words = resume_str.split(' ')
    quant_words = []
    substrings = ['%','$','percent','dollar','CAD','USD']

    for word in words:
        for substr in substrings:
            if substr in word:
                quant_words.append(word) 
    return(quant_words) 

def check_email(resume_str: str) -> Tuple[str, str]:
    """
    Checks if string contains valid email address

    Parameters
    ----------
    resume_str :  str
        The resume parsed as string.
        
    Returns
    -------
    tuple
    (str, str)	
    """
    
    regex = r'[\w\.-]+@[\w\.-]+\.\w+'    
    if(re.search(regex,resume_str)):  
        email = re.findall(regex,resume_str)
        return("valid",email)  
          
    else: 
        return("invalid","blank")  


def check_linkedin(resume_str: str) -> str:
    """
    Checks if string contains LinkedIn url.

    Parameters
    ----------
    resume_str :  str
        The resume parsed as string.
        
    Returns
    -------
    str	
    """
    #this can be improved, not very robust
    search_for = 'linkedin.com'
    if search_for in resume_str:
        return 'contains'
    else:
        return 'does not contain'
