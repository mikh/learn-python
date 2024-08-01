"""Module try_filter tests out filter functionality."""

data = [1, 4, 6, 3, 11, 99, 23, 12]

assert list(filter(lambda x: x % 2 != 0, data)) == [1, 3, 11, 99, 23]
