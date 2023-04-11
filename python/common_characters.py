"""
write a function that takes in a list of strings and returns a list of common characters.
"""
import unittest


def common_characters(strings):
    if not strings:
        return []
    # Find the intersection of the sets of characters for all strings
    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    # Convert the set to a list and return it in order
    common_characters = [char for char in strings[0] if char in common_chars]
    # dict.fromkeys is a method that creates a new dictionary with keys from the iterable/list and sets their value to the given value
    return list(dict.fromkeys(common_characters))


class TestCommonCharacters(unittest.TestCase):
    def test_common_characters(self):
        self.assertEqual(common_characters(['abc', 'bcda', 'cdba']), ['a', 'b', 'c'])
        self.assertEqual(common_characters(['abxel', 'bxel', 'cxelb', 'dxelb']), ['b', 'x', 'e', 'l'])
        self.assertEqual(common_characters(['abc', 'def', 'ghi']), [])
        self.assertEqual(common_characters(['abc', 'cba']), ['a', 'b', 'c'])
        self.assertEqual(common_characters(['aaa', 'aa', 'a']), ['a'])
        self.assertEqual(common_characters(['abc']), ['a', 'b', 'c'])
        self.assertEqual(common_characters([]), [])


if __name__ == '__main__':
    unittest.main()