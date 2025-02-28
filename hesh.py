import hashlib
from string import ascii_letters


def my_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


table = {}

for let1 in ascii_letters:
    for let2 in ascii_letters:
        for let3 in ascii_letters:
            password = let1 + let2 + let3
            table[password] = my_hash(password)
print(table)