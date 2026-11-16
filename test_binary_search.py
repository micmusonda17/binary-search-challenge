# Unit tests for binary_search.py

import unittest

from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

    def test_finds_item_in_the_middle(self):
        self.assertEqual(binary_search(self.numbers, 16), 4)

    def test_finds_first_item(self):
        self.assertEqual(binary_search(self.numbers, 2), 0)

    def test_finds_last_item(self):
        self.assertEqual(binary_search(self.numbers, 91), 9)

    def test_returns_minus_one_when_missing(self):
        self.assertEqual(binary_search(self.numbers, 7), -1)

    def test_target_smaller_than_every_item(self):
        self.assertEqual(binary_search(self.numbers, 1), -1)

    def test_target_bigger_than_every_item(self):
        self.assertEqual(binary_search(self.numbers, 100), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)

    def test_single_item_list(self):
        self.assertEqual(binary_search([7], 7), 0)
        self.assertEqual(binary_search([7], 3), -1)

    def test_negative_numbers(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 10], -4), 1)

    def test_matches_list_index_on_a_large_list(self):
        big_list = list(range(0, 10000, 3))
        for value in [0, 3, 2997, 9999]:
            self.assertEqual(binary_search(big_list, value), big_list.index(value))
        self.assertEqual(binary_search(big_list, 4), -1)


if __name__ == "__main__":
    unittest.main()
