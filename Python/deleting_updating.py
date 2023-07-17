#Python program to update
#character of a string

string1 = "hello, I'm a Pythonista"
print("Initial string: ")
print(string1)

#Updating a character of the string
#As python strings are immutable , the don't support item updation directly
#there are following two ways
#1
list1 = list(string1)
list1[1] = 'E'
string2 = ''.join(list1)
print("\nUpdating character at 2nd index: ")
print(string2)

#2
string3 = string1[0:1] + 'E' + string1[2:]
print(string3)
