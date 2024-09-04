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


if __name__ == "__main__":
    # for j in generate(300, 13):
    #     print(j)
    num_squared_lc = [x**2 for x in range(100)]
    num_squared_gc = (x**2 for x in range(100))

    print("lc", get_size_recursive(num_squared_lc))
    print("gc", get_size_recursive(num_squared_gc))
