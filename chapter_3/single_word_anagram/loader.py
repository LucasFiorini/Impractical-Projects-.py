import sys

def load(file):
	try:
		with open(file) as in_file:
			loaded_txt = [word for line in in_file for word in line.split()] 
			return loaded_txt
	except IOError as e:
		print("{}\n Error opening {}. Terminating program.".format(e, file), file = sys.stderr)
		sys.exit(1)

