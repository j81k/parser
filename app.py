import sys
import os.path
import re
import math

sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/util')
import helpers


filename = './gmail_uber.json';
regexp = re.compile('(\|  (.*?) [0-9]{0,6}, India)', re.IGNORECASE)
#8:56pm |  Vijaya Raghava Rd, Parthasarathi Puram, T Nagar, Chennai, Tamil Nadu 600017, India  09:15pm |

split = 4
thresold = 80

def split_str(string):
	
	char = ''
	segments = []
	for k,c in enumerate(string):
		if k%split == 0 and k > 0:
			segments.append(char)
			char = ''
		
		char += c

	return segments
			
def percentage(segments1, segments2):
	count1 = len(segments1)
	count2 = len(segments2)

	if count1 <= count2:
		segments = segments1
		alt_segments = segments2
		count = count1;
	else:
		segments = segments2
		alt_segments = segments1
		count = count2;

	match_count = 0;
	for k,segment in enumerate(segments):
		if alt_segments[k] == segment:
			match_count += 1;

	return math.ceil((match_count/count)*100)		
	

def compare_str(string1, string2):
	string1 = helpers.alpha_numeric(string1)
	string2 = helpers.alpha_numeric(string2)

	segments1 = split_str(string1)
	segments2 = split_str(string2)

	if percentage(segments1, segments2) >= thresold:
		return True

	return False	


def unique(a):
	
	i1 = 0
	for i in a[i1:-1]:
		i2 = i1+1
		for k in a[i2:]:
			if compare_str(a[i1],a[i2]):
				#print('Removing ...'+a[i2], "\t Index: %s" %i2)
				a.pop(i2)
			else:
				i2 += 1

		i1 += 1

	return a
				

def file_to_str(filename):
	with open(filename) as f:
		return f.read()

def extract(contents):
	return (match[0].strip('|, ') for match in re.findall(regexp, contents))		



if __name__ == '__main__':
	
	i = 0;
	fh = open('output.txt', 'w')

	contents = list(extract(file_to_str(filename)))
	contents = unique(contents)
	for line in contents:
		i += 1;
		fh.write("%s" % i +". "+line+"\n")

	


