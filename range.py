"""
In 3.X range is an iterable, that generates items on demand, so we need to wrap it in a list call to display its results all at once.
"""
x = list(range(5)), list(range(2,5)), list(range(0,10,2))
print(x)
