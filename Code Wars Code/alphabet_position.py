# from string import ascii_lowercase as ac

# def alphabet_position(text):
#     solution = ''
#     num_list = []
#     text = text.lower()

#     for char in text:
#         if char in ac:
#             num_list.append(str(ac.index(char) + 1 ))

#     solution = " ".join([val for val in num_list])

#     return solution

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# text = "The sunset sets at twelve o' clock."
text = "The narwhal bacons at midnight."
print(alphabet_position(text))