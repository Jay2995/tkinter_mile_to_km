def add(*arg):
    result = 0;
    for n in arg:
        result += n
    return result;



print(add(1,2,3,4,5))


def calculuate(**kwargs):
    print(kwargs);
    for nig, nigz in kwargs.items():
        print(nig);
        print(nigz);


calculuate(add=5, multiply=3);