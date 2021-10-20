from contextlib import contextmanager

@contextmanager
def get_one():
    yield 1

with get_one() as n1, \
     get_one() as n2, \
     get_one() as n3:
    assert n1 + n2 + n3 == 3


# Still unrecognized syntax as of PyCharm Community 2021.2.3
with (
    get_one() as n1,
    get_one() as n2,
    get_one() as n3
):
    assert n1 + n2 + n3 == 3
