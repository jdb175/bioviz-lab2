#Process.py
import getopt
import sys
import re

def main():
	"""
	Handle cli arguments
	"""
	# Parse parameters
	names_file = None
	data_file = None
	out_file = None
	options = 'd:n:o:'
	try:
		optlist, args = getopt.getopt(sys.argv[1:], options)
	except getopt.GetoptError as error:
		print str(error)
		sys.exit(RTN_INIT_FAIL)

	for opt, arg in optlist:
		if opt in ('-n'):
			names_file = arg
		elif opt in ('-d'):
			data_file = arg
		elif opt in ('-o'):
			out_file = arg

	if(data_file and names_file and out_file):
		process(data_file, names_file, out_file)
	else:
		print "Please input a data file, names file, and output file"

def process(data_loc, names_loc, out_loc):
	#process header info
	firstline, names, types = processHeaders(names_loc)
	#process data
	data_text = processData(data_loc, types)

	#output data
	csv_file = firstline+ "\n" + data_text
	f = open(out_loc, 'w')
	f.write(csv_file)

def processHeaders(names_loc):
	"""
	Method for processing the header data
	"""
	csv_file = ""
	names = []
	types = []

	#Read in Headers
	f = open(names_loc, 'r')
	is_names = False
	for line in f:
		if is_names:
			#print line
			if line == "\n":
				break
			#match parts
			match = re.search('[0-9]+\. (.+?)[\t\n\r\f\v:]+(.+)', line)
			name = match.group(1).strip()
			category = match.group(2).strip().split(" ")[0]
			#append them into lists
			names.append(name)
			types.append(category)
		#Find the start of headers
		elif line == "7. Attribute Information: (name of attribute and type of value domain)\n":
			is_names = True

	#Add headers to file
	csv_file+=names.pop()
	for name in names:
		csv_file+= ', ' + name

	f.close()
	return csv_file, names, types

def processData(data_loc, types):
	data_text = ""

	#read in each line
	f = open(data_loc, 'r')
	first = True
	for line in f:
		#now split it by commas
		entries = line.split(",")
		#create line text
		line = ""
		if not first:
			line += "\n"
		else:
			first = False
		#process each
		for i in range(0, len(entries)):
			put = processEntry(entries[i], types[i])
			if i is not 0:
				line+=","
			line += put
		data_text+=line

	f.close()
	return data_text

def processEntry(value, entrytype):
	if entrytype == "Boolean":
		return str(value == "1")
	else:
		return value

if __name__ == "__main__":
    main()