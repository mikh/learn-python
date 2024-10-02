"""Module try_generator explores generators."""

from typing import Any

import sys


def generate(limit: int, step: int):
    """Generate numbers."""
    i = 0
    while i < limit:
        i += step
        yield i


def get_size_recursive(o: Any):
    """Recursively get size."""
    size = sys.getsizeof(o)
    if isinstance(o, list):
        for x in o:
            size += get_size_recursive(x)
    return size


def is_multiple_of_11(v: int) -> bool:
    """Is it a multiple of 11"""
    return v % 11 == 0


def infinite_11s():
    num = 0
    while True:
        if is_multiple_of_11(num):
            print(f"{num} is a multiple of 11")
            i = yield num
            if i is not None:
                print(f"set num = {i}")
                num = i
            else:
                print("i is None")
        num += 1
        print(f"num = {num}")


def eleven_loop():
    ele_gen = infinite_11s()
    counter = 0
    for i in ele_gen:
        print(i)
        digits = len(str(i))
        print(f"Send response = {ele_gen.send(10 ** (digits))}")
        counter += 1
        if counter > 4:
            break


if __name__ == "__main__":
    # for j in generate(300, 13):
    #     print(j)
    # num_squared_lc = [x**2 for x in range(100)]
    # num_squared_gc = (x**2 for x in range(100))

    # print("lc", get_size_recursive(num_squared_lc))
    # print("gc", get_size_recursive(num_squared_gc))

    eleven_loop()
