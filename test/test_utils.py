import unittest

from pypaillier import utils

class TestUtils(unittest.TestCase):
    def test_universal_mod_inverse(self):
        self.assertEqual(utils.mod_inv(3, 11), 4)

    def test_lcm(self):
        self.assertEqual(utils.lcm(3, 4), 12)
        self.assertEqual(utils.lcm(3, 6), 6)
        self.assertEqual(utils.lcm(28, 12), 84)


if __name__ == '__main__':
    unittest.main()
