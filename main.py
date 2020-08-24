#create a function all cpital letter and 
#punctuation in a string. Return the clean string.

def clean_str1(str1):
    new_str = str1 
    for i in str1:
        if i.isupper():
            new_str = str1.replace(i, '')

    return new_str

print (clean_str1('Call Me Maybe'))            