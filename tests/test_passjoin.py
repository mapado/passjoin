import unittest
from Levenshtein import distance
from passjoin import Passjoin


class TestPassjoin(unittest.TestCase):

    def test_addition(self):
        """"""
        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('giraf'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('irafe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('girfe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('grfe'), set())

    def test_suppression(self):
        """"""
        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('girafes'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('ggirafe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('giirafe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('giraafes'), set())

    def test_substitution(self):
        """"""
        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('girafr'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('sirafe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('girzfe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('gorefe'), set())

    def test_multi(self):
        """"""
        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 2, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('irafr'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('giirofr'), set())

    def test_special_cases(self):
        """"""
        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 0, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('girafe'), {'girafe'})
        self.assertSetEqual(passjoin_index.get_word_variations('giraf'), set())

        passjoin_index = Passjoin([], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations('giraf'), set())

        passjoin_index = Passjoin(['girafe', 'lion', 'tiger'], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations(''), set())

        passjoin_index = Passjoin(['girafe', 'lion', 'tiger', 'a'], 1, distance)
        self.assertSetEqual(passjoin_index.get_word_variations(''), {'a'})

