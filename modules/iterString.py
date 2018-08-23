from string import ascii_lowercase
import itertools

def iter_all_strings(size):
    while True:
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)