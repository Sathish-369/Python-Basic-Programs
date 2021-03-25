def Remove (tuples):
    tuples = [t for t in tuples if t ]
    return tuples

tuples = [(),('sat', 28, '30'), (), ('ame', 'ammu'), ((())), ('sath', '88','satuu'), (" ", " "), ()]
print(Remove(tuples))
