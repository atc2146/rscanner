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
