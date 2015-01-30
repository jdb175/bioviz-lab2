#Process.py
import getopt
import sys
import re

def main():
	"""
	Handle cli input and start
	"""
	# Parse parameters
	data_file = None
	out_file = None
	options = 'd:n:o:'
	try:
		optlist, args = getopt.getopt(sys.argv[1:], options)
	except getopt.GetoptError as error:
		print str(error)
		sys.exit(RTN_INIT_FAIL)

	for opt, arg in optlist:
		if opt in ('-d'):
			data_file = arg
		elif opt in ('-o'):
			out_file = arg

	if(data_file and out_file):
		process(data_file, out_file)
	else:
		print "Please input a data file and output file"

def process(data_loc, out_loc):
	"""
	Process data from input file into output file
	"""
	#process data
	data_text = processData(data_loc)

	#output data
	csv_file = "animal name, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize, type\n" + data_text
	f = open(out_loc, 'w')
	f.write(csv_file)

def processData(data_loc):
	"""
	Process line-by-line data from file
	"""
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
			#format by type
			put = processEntry(entries[i], types[i])
			if i is not 0:
				line+=","
			line += put
		data_text+=line

	f.close()
	return data_text

def processEntry(value, entrytype):
	"""
	Convert individual entries based on type
	"""
	if entrytype == "Boolean":
		return str(value == "1")
	else:
		return value

if __name__ == "__main__":
    main()