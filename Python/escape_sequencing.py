#Python program for escape
#sequencing of string

string1 = '''I'm a  "Pythonista"'''
print("Initial string with the use of triple quote: ")
print(string1)

#Escaping single Quote
string1 = 'I\'m a "Pythonista"'
print("\nEscaping single quote: ")
print(string1)

#Escaping double quotes
string1 = "I'm a \"Pythonista\""
print("\nEscaping double quote: ")
print(string1)

#Printing paths with the use
#escape sequences
string1 = "C:\\python\\Programming\\"
print("\nEscaping backslashes: ")
print(string1)

#Printing paths with the use
#of Tabs
string1 = "Hi\tPython"
print("\nTab: ")
print(string1)

#Printing paths with the use
#of new line
string1 = "Python\nProgramming"
print("\nNew line: ")
print(string1)
