from builtins import object


class IterableExample(object):
    def __init__(self):
        self.i = 0

    def __next__(self):
        self.i = self.i + 5
        if self.i >= 100:
            raise StopIteration
        yield self.i

    def __iter__(self):
        return self


iterable = IterableExample()
for val in iterable:
    print(next(val))
