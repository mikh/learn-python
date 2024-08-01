"""Module try_filter tests out filter functionality."""

from typing import List

import random
import time

import tqdm


def base():
    """Try out a basic test."""
    data = [1, 4, 6, 3, 11, 99, 23, 12]

    assert list(filter(lambda x: x % 2 != 0, data)) == [1, 3, 11, 99, 23]


def generate_large_input(start: int = 1, end: int = 10000, n: int = 1000000):
    """Generates a large random input."""
    return [random.randint(start, end) for _ in range(n)]


def test_filter_lambda(data: List[int]) -> float:
    """Tests how fast filter performs if using a lambda."""
    start = time.perf_counter()

    filter(lambda x: x % 2 != 0, data)

    return time.perf_counter() - start


def test_filter_function(data: List[int]) -> float:
    """Tests how fast filter performs if using a function."""

    def _filter_func(x: int) -> bool:
        """Checks mod of value."""
        return x % 2 != 0

    start = time.perf_counter()
    filter(_filter_func, data)
    return time.perf_counter() - start


def test_generator(data: List[int]) -> float:
    """Tests how fast a generator will work."""
    start = time.perf_counter()

    _ = (x for x in data if x % 2 != 0)

    return time.perf_counter() - start


def test_generator_function(data: List[int]) -> float:
    """Tests how fast generator performs if using a function."""

    def _filter_func(x: int) -> bool:
        """Checks mod of value."""
        return x % 2 != 0

    start = time.perf_counter()

    _ = (x for x in data if _filter_func(x))

    return time.perf_counter() - start


if __name__ == "__main__":
    # base()
    tests = 10
    counts = {"filter-lambda": 0, "filter-func": 0, "generator": 0, "generator-func": 0}

    for _ in tqdm.tqdm(range(tests)):
        input_data = generate_large_input(n=10000000)
        counts["filter-lambda"] += test_filter_lambda(input_data)
        counts["filter-func"] += test_filter_function(input_data)
        counts["generator"] += test_generator(input_data)
        counts["generator-func"] += test_generator_function(input_data)

    print(f"Filter Lambda: {counts['filter-lambda']/tests}")
    print(f"Filter Function: {counts['filter-func']/tests}")
    print(f"Generator: {counts['generator']/tests}")
    print(f"Generator Function: {counts['generator-func']/tests}")
