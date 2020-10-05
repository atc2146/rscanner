import pdfplumber
import docx2txt
import os


def read_file(path: str, file_extension: str) -> str:
	"""
	Reads a file as a string.
	
	Parameters
	----------
	path : str
		The path to the file.

	file_extension : str
		The file's extension. Includes the period.

	Returns
	-------
	str
	
	Examples
	--------
	
	"""
    if file_extension=='.docx':
        data = docx2txt.process(path)
    elif file_extension=='.pdf':
        pdf = pdfplumber.open(path)
        page = pdf.pages[0]
        data = page.extract_text()
        pdf.close()
    else:
        with open(path) as file:
            data = file.read()
	
	return data
    
def check_file_ext(path: str) -> str:
    """
    Determines if file extension is valid. Raises
    TypeError if it is not.

    Parameters 
    ----------
    path : str
        The path to the file

    Returns
    -------
    str

    Examples
    --------

    """
    filename, file_extension = os.path.splitext(path)
    valid_file_extensions = ['.pdf', '.docx', '.txt']

    if file_extension in valid_file_extensions:
        data = read_file(path, file_extension)
    else:
        error_msg_file_extension = ', '.join(valid_file_extensions)
        raise TypeError(f'Please input either a one of the following file formats: {error_msg_file_extension}')

    return(data)