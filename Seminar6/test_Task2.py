import pytest
from Task2 import count_words


@pytest.mark.parametrize('words, expected_result', [('дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул', {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3})])
def test_conuting(words, expected_result):
    assert count_words(words) == expected_result


#print(count_words('дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'))
