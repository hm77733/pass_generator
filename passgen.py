#Password Generator Project
import random
MIN_LETTER = 8
MAX_LETTER = 10
MIN_SYMBOL = 2
MAX_SYMBOL = 4

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    letters_list = [random.choice(letters) for char in range(random.randint(MAX_LETTER, MAX_LETTER))]
    print(letters_list)
    sym_list = [random.choice(symbols) for char in range(random.randint(MIN_SYMBOL, MAX_SYMBOL))]
    num_list = [random.choice(numbers) for char in range(random.randint(MIN_SYMBOL, MAX_SYMBOL))]

    password_list = letters_list + sym_list + num_list

    random.shuffle(password_list)

    password = ''.join(password_list)

    return  password

