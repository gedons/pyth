def announce(f):
	def wrapper():
		print("About to run the function")
		f()
		print("Done with the function")
	return wrapper

# the input (f) value
@announce
def hello():
	print("hello world")

hello()