def sample():
    yield 1
    yield 2
    yield 3
    yield 4
inp = sample()
print(next(inp))
print(next(inp))
print(next(inp))
print(next(inp))

