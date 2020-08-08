import re

def FilePrep(resume: str) -> str:
    """
	Reads resume string and removes special characters.
	
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
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', resume).lower()

    return (cleaned_str)