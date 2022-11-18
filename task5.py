import random
from random import sample
def get_random_password() -> str:
    alph = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''
    i = random.sample(alph, 8)
    password += str(i)
    return password
print(get_random_password())
