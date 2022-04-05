import re

def to_camel_case(text):
    #your code here
    camel_case = ''

    if text == '':
        return ''

    split_txt = re.split("[-_]", text)

    for char in split_txt:
        if split_txt.index(char) != 0:
            camel_case += char.capitalize()
        else:
            camel_case += char
    return camel_case

# text = "the_stealth_warrior"
text = "The-Stealth-Warrior"
print(to_camel_case(text))

# text = "python is, an easy;language; to, learn."
# print(re.split('[;,]', text))