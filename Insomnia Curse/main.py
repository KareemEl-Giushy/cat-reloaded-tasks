from HarmDragons import harm_dragons
import unittest

class HarmDragons(unittest.TestCase):

    def test_1(self):
        res  = harm_dragons(1, 2, 3, 4, 12)

        self.assertEqual(res, 12)

    def test_2(self):
        res = harm_dragons(2, 3, 4, 5, 24)

        self.assertEqual(res, 17)

if __name__ == '__main__':
    unittest.main()