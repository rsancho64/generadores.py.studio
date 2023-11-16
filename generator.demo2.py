#! /usr/bin/python3

# """las listas ocupan mucho mas que los generadores"""
# import sys
# l = [n * 2 for n in range(1000)]  # lista
# g = (n * 2 for n in range(1000))  # generador
# print(sys.getsizeof(l))
# print(sys.getsizeof(g))

# mas pequeños
# l = [n * 2 for n in range(10)]  # lista
g = (n * 2 for n in range(10))  # generador
for item in g:
    print(item, end=", ")


