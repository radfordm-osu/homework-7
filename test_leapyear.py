import unittest
import leapyear

class leapyeartester(unittest.TestCase):
    def test_leapyear_204(self):
        result = leapyear.leapyear(204)
        self.assertEqual(result, True)

    if __name__ == "__main__":
        unittest.main()
