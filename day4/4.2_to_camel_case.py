def to_camel_case(text):
    camel_case = ''
    indices = []

    for i in range(len(text)):
        if text[i].isalpha():
            camel_case += text[i]
        else:
            indices.append(len(camel_case))

    for index in indices:
        if index < len(camel_case):
            camel_case = camel_case[:index] + camel_case[index].upper() + camel_case[index + 1:]

    return camel_case



print(to_camel_case('what_is_your_name?'))


'''
    -Slice each word at the hyphen or underscore
        find the index of each special character.
        Add one to the special char to get the next one
        capitalize the next character
        remove the hyphen
    -capitalize each word after each hyphen
    

Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''