class PairIterator:
    def __init__(self, *values):
        self.values = list(values)
        if len(self.values) % 2 != 0:
            self.values.append(None)
        self.index = 0

    def __next__(self):
        if self.index + 1 < len(self.values):
            result = (self.values[self.index], self.values[self.index + 1])
            self.index += 2
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


pair_iter = PairIterator(1, 2, 3, 4)
for pair in pair_iter:
    print(pair)

print()

pair_iter = PairIterator(1, 2, 3, 4, 5)
for pair in pair_iter:
    print(pair)
