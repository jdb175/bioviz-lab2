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
	#process data
	data_text = processData(data_loc)

	#output data
	csv_file = "type, animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize\n" + data_text
	f = open(out_loc, 'w')
	f.write(csv_file)

def processData(data_loc):
	data_text = ""
	types = ['Unique', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Boolean', 'Numeric', 'Boolean', 'Boolean', 'Boolean', 'Numeric']

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