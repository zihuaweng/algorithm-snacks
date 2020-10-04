"""
There are four ways to build an iterative function:

1. create a generator (uses the yield keyword)
2. use a generator expression (genexp)
3. create an iterator (defines __iter__ and __next__ (or next in Python 2.x))
4. create a class that Python can iterate over on its own (defines __getitem__)

https://stackoverflow.com/questions/19151/build-a-basic-python-iterator

"""

# 1. create a generator (uses the yield keyword)
def uc_gen(text):
    for char in text.upper():
        yield char


iterator = uc_gen('abc')
for char in iterator:
    print(char, end=' ')
print()
print('------')


# 3. create an iterator (defines __iter__ and __next__ )
class uc_iter:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


iterator = uc_iter('abc')
for char in iterator:
    print(char, end=' ')
print()
print('------')


iterator = iter('abc')
for char in iterator:
    print(char, end=' ')
print(iterator)
print()
print('------')
