


def strip_input(name):
    """This will lowercase all letters and then strip nonletters from the string"""
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
    """compares the parameter string and its reverse to see if it's palindrome"""
    print ("is_palindrome was called")
    #name[begin:end:step] is outputting the string 'name' in reverse. 
    if strip_input(name) == strip_input(name[::-1]):    
        return print("is a palindrome!")
    else:
        return print("is not a palindrome!")

while True:
    name = input("Enter a word or sentence and see if it's palindrome [type 'quit' to end]: ")
    #if the user inputs 'quit' the loop will terminate 
    if name == 'quit':
        break
    #if the user does not enter anything, they will be prompted to retry, and the loop will restart    
    if name == "":
        print ("You didn't enter anything, let's start over!")
        continue    
    is_palindrome(name)

