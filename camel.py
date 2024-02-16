# create a function that takes a string as input and returns a string with alternating upper and lower case letters

def camel(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].lower()
        else:
            new_string += string[i].upper()
    return new_string

# write a print statement that calls the camel function with input when the script is ran

# take input as a string from the user and assign it to a variable
user_input = input("Enter a string: ")

print(camel(user_input))