def greet(name, adjective, punctuation):
    print(f"Hello, {name}{punctuation} You are {adjective}{punctuation}")

greet("Alice", "rad", "!")
greet("rad", "!", "Alice")
greet("!", "Alice", "rad")

print("\n\n\n")

def getInfo(name, phoneNum = "N/A"):
    print(f"{name}\'s number is {phoneNum}")
    
getInfo("Cherry")
getInfo("Steve", "867-5309")
getInfo(phoneNum="555-5555", name = "Yvette")

print("\n\n\n")

def sum_all(*args):
	result = 0
	for num in args:
		result += num
	return result

print(sum_all(1, 2, 3, 4, 5))

print("\n\n\n")


def display_info(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")


print("\n\n\n")

def print_args_and_kwargs(*args, **kwargs):
	print("Positional arguments:")
	for arg in args:
		print(arg)
	
	print("Keyword arguments:")
	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_args_and_kwargs(1, 2, 3, name="Alice", age=30)


print("\n\n\n")

def print_coordinates(x, y, z, w):
	print(f"X: {x}, Y: {y}, Z: {z}, W: {w}")

coordinates = [1, 2, 3, 4]

print_coordinates(*coordinates)



print("\n\n\n")

def print_values(a, b, c, d):
	print(a, b, c, d)

arguments = {'b': 10, 'a': 20, 'c': 30, 'd': 40}

print_values(**arguments)


