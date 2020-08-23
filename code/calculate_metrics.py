from typing import Tuple

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
        num_of_words = resume_str.split(' ')
        return len(resume_str), num_of_words
    except:
        raise TypeError('Not a string')

def resume_length_checker(resume_words: int) -> str:
    """
	Returns an evaluation of the resume's length.
	
	Parameters
	----------
	resume_words : int
		The number of words in the resume
		
	Returns
	-------
	str	
	"""
    if (resume_words >= 0 and resume_words <= 325):
        return 'Too Short'
    elif (resume_words > 325 and resume_words <= 650):
        return 'Ideal'
    else:
        return 'Too long'

def count_quantifiable_metrics(resume_str: str):
    """
	Counts the number of quantifiable metrics in the resume.  Based on string matches of
    keywords such as percent, %, $, dollars, USD, etc.
	
	Parameters
	----------
	resume_str :  str
		The resume parsed as string.
		
	Returns
	-------
	int	
	"""
    pass