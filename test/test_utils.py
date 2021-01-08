import unittest

from pypaillier import utils

class TestUtils(unittest.TestCase):
    def test_universal_mod_inverse(self):
        self.assertEqual(4, utils.mod_inv(3, 11))

    def test_lcm(self):
        self.assertEqual(12, utils.lcm(3, 4))
        self.assertEqual(6, utils.lcm(3, 6))
        self.assertEqual(84, utils.lcm(28, 12))


if __name__ == '__main__':
    unittest.main()
