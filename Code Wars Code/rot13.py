from string import ascii_uppercase, ascii_lowercase

ALPHABET = ascii_lowercase + ascii_uppercase

def rot13(message):
    encrypt_msg = ""

    for char in message:
        if char in ALPHABET:
            if char in ascii_lowercase:
                ascii_lower_index = ascii_lowercase.index(char)
                try:
                    rot_lower_shift = ascii_lower_index + 13
                    encrypt_msg += ascii_lowercase[rot_lower_shift]
                except:
                    rot_lower_shift = ascii_lower_index - 26
                    encrypt_msg += ascii_lowercase[rot_lower_shift - 13]


            if char in ascii_uppercase:
                ascii_upper_index = ascii_uppercase.index(char)
                try:
                    rot_upper_shift = ascii_upper_index + 13
                    encrypt_msg += ascii_uppercase[rot_upper_shift]
                except:
                    rot_upper_shift = ascii_upper_index - 26
                    encrypt_msg += ascii_uppercase[rot_upper_shift - 13]

        else:
            encrypt_msg += char
    
    return encrypt_msg

print(rot13("Test"))


