"""You should always prefer to use built-in syntax for slice"""
my_numbers = (4, 5, 3, 9)
print(my_numbers[-1])
print(my_numbers[-3])

my_numbers = (1, 1, 2, 3, 5, 8, 13, 21)
print(my_numbers[2:5])

print(my_numbers[:3])
print(my_numbers[3:])

print(my_numbers[::])  # also returns a copy
print(my_numbers[1:7:2])  # step, how many elements to jump when iterating over the interval.

interval = slice(1, 7, 2)
print(my_numbers[interval])
