from dataclasses import dataclass


def f(first, second, third):
    print(first)
    print(second)
    print(third)


l = [1, 2, 3]
f(*l)


def show(e, rest):
    print("Element: {0} - Rest: {1}".format(e, rest))


first, *rest = [1, 2, 3, 4, 5]
print(show(first, rest))

*rest, last = range(6)
print(show(last, rest))

first, *middle, last = range(6)
print(first, middle, last)

first, last, *empty = 1, 2
print(first, last, empty)


# def function(**kwargs):
#     print(kwargs)


def function(timeout=5, **kwargs):
    return kwargs



print(function(key="value"))

USERS = [
    (i, f"first_name_{i}", f"last_name_{i}")
    for i in range(1_000)
]


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str


def bad_users_from_rows(dbrows) -> list:
    """A bad case (non-pythonic) of creating ''User''s from DB rows."""
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_row(dbrows) -> list:
    """Create ''User''s from DB rows."""
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]
    # [User(*row) for row in dbrows]

def my_function(x, y):
    print(f"{x=}, {y=}")

# my_function(1, 2)
# my_function(x=1, y=2)
# my_function(y=2, x=1)
# my_function(1, y=2)


def my_function_2(x, y, /):
    """strictly positional parameters -> /"""
    print(f"{x=}, {y=}")

my_function_2(1, 2)
my_function_2(x=1, y=2)
