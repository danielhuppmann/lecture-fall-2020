from core import foo


def test_foo():
    assert foo(2) == 3

def test_foo_two_args():
    assert foo(2, 3) == 6
