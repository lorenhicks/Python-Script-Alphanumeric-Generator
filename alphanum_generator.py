import random
import string

def generate_alphanum_string(length):
    characters = string.ascii_letters.upper() + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

num_sets = 15
string_length = 7

for _ in range(num_sets):
    random_string = generate_alphanum_string(string_length)
    print(random_string)
