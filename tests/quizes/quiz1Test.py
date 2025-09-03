from checkpy import *

@test()
def test1():
    """Checking input: 7"""
    output = outputOf(stdinArgs=[7])
    assert "[1, 4, 9, 16, 25, 36, 49]" == output.strip()

@test()
def test2():
    """Checking input: 9"""
    output = outputOf(stdinArgs=[9])
    assert "[1, 4, 9, 16, 25, 36, 49, 64, 81]" == output.strip()