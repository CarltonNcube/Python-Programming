#Python program to delete
#charactors from a string

string1 = "Hello, I'm a Pythonista"
print("Initial string: ")
print(string1)

#deleting a character
#of the string

string2 = string1[0:2] + string1[3:]
print("\nDeleting character on the second index: ")
print(string2)

