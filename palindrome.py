
name = input("Enter a word and see if it's palindrome: ")

def strip_input(name):
    import re
    print ("strip_input was called")
    #.lower will take the entire string and make all cases lower
    name = name.lower()
    print(name)
    #.replace takes every white space and makes it 'None' or empty
    name = name.replace(" ","")
    print(name)
    #re.sub takes the sub function from re and transform all special characters to 'None' or empty.
    name = re.sub(r'[^a-zA-Z0-9 ]',r'',name)
    print(name)
    return name

def is_palindrome(name):
    print ("is_palindrome was called")
    #name[begin:end:step] is outputting the string 'name' in reverse. 
    if strip_input(name) == strip_input(name[::-1]):
        return print("This was a palindrome!")
    else:
        return print("This was NOT a palindrome!")

is_palindrome(name)
