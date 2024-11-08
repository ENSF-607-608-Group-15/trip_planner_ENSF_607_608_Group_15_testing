import random
import string


def generate_random_string(size):
    random_text = ''.join(random.choices(
        string.ascii_letters + string.digits, k=size))
    return random_text
