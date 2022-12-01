# import a function(square) from another file(functions)
from functions import square

for i in range(10):
 	print(f"the square of {i} is {square(i)}")