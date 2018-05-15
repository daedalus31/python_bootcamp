def find_words(string, no_of_letters):
    return set([w for w in string.split() if len(w) == no_of_letters])


def test_find_words():
    assert find_words('', 4) == set()
    assert find_words('ala ma kota a kot ma ale', 3) == {'ale', 'kot', 'ala'}
    assert find_words('ala ma kota a kot ma ale', 10) == set()
