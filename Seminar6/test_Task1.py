import pytest
from Task1 import calculate


@pytest.mark.parametrize('expression, expected_result', [('2+2', 4),
                                                         ('1+2*3', 7),
                                                         ('1-2*3', -5),
                                                         ('1+2*3', 7),
                                                         ('(1+2)*3', 9)])
def test_calculating(expression, expected_result):
    assert calculate(expression) == expected_result


# print(calculate('2+2'))  # 4
# print(calculate('1+2*3'))  # 7
# print(calculate('1-2*3'))  # -5
# print(calculate('1+2*3'))  # 7
# print(calculate('(1+2)*3'))  # 9
