from tika import parser
import docx2txt
import os

def read_txt_file(path: str) -> str:
	"""
	Reads a text file as a string.
	
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
	with open(path) as file:
		data = file.read()
	
	return data


def read_pdf_file(path: str) -> str:
    """
    Reads a PDF file and extracts the text.

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
    raw = parser.from_file(path)

    text = (raw['content'])

    return text
    

def read_docx_file(path: str) -> str:
    """
    Reads a docx file and extracts the text.

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
    my_text = docx2txt.process(path)
    
    return(my_text)
    
def check_file_ext(path: str) -> str:
    """
    Determines the file extension and extracts the text.

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
    filename, file_extension = os.path.splitext(path)

    if file_extension == '.pdf':
        data = read_pdf_file(path)
    elif file_extension == '.docx':
        data = read_docx_file(path)
    elif file_extension == '.txt':
        data = read_txt_file(path)
    else: 
        print('Please input either a pdf, docx, or txt file')

    return(data)


test = check_file_ext('sample_resume.pdf')

print(test)

