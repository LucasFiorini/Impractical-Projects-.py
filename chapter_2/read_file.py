import sys

def load(file):
	try:
		with open(file) as in_file:
			load_txt = in_file.read().strip().split('\n')
			loaded_txt = [x.lower() for x in load_txt]
			return loaded_txt
	except IOError as e:
		print("{}\nError opening {}. Terminating program.".format(e,file),file = sys.stderr)
		sys.exit(1)
