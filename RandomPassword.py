import random
import string

# dictionary with the characters with which to build the passwords
DICTIONARY = {'upper': list(string.ascii_uppercase), 'lower': list(string.ascii_lowercase), 'digits': list(string.digits), 'espec': list('!@#$^%&()*/')}
OPTIONS = list(DICTIONARY.keys()) # List With the dictionary keys


# Counts characters of the same type
def count_character(password: list, key: str) -> int:
    count = 0
    search_list = DICTIONARY.get(key)
    for e in password:
        if e in search_list:
            count += 1
    return count


# We change the password to make sure that in case it does not happen, it has at least one character of each type
def transform_password(password: list) -> str:
    may, min, digit, esp = count_character(password, 'upper'), count_character(password, 'lower'), count_character(password, 'digits'), count_character(password, 'espec')
    if may == 0:
        password.remove
        password.append(random.choice(DICTIONARY.get('upper')))
    if min == 0:
        password.remove
        password.append(random.choice(DICTIONARY.get('lower')))
    if digit == 0:
        password.remove
        password.append(random.choice(DICTIONARY.get('digits')))
    if esp == 0:
        password.remove
        password.append(random.choice(DICTIONARY.get('espec')))
    # We rearrange it to make it even more random
    random.shuffle(password)
    return ''.join(password)
    

# Characters are added to the password, randomly taking a character from a list randomly taken from the dictionary
def generate_password(lenght: int) -> str:
    password = []
    for i in range (lenght):
        password.append(random.choice(DICTIONARY.get(random.choice(OPTIONS))))
    return transform_password(password)


# The only thing that the user is asked to do is give us the length of the password they want to generate.
def random_password():
    length = int(input('Introduzca la Cantidad de digitos para su Contraseña:'))
    while length:
        password = generate_password(length)
        print(password)
        length = int(input('Introduzca la Cantidad de digitos para su Contraseña:'))

random_password()