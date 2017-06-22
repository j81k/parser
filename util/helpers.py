import re

def alpha_numeric(string):
	regexp = re.compile('[0-9a-z]+', re.IGNORECASE)
	return "".join(re.findall(regexp, string))
