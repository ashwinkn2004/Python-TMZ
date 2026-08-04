def sample():
    yield 1
    yield 2
    yield 3
    yield 4

print(next(sample()))
print(next(sample()))
print(next(sample()))
print(next(sample()))