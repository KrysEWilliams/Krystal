import unittest
from File1 import my_square_root

class ExampleTest(unittest.TestCase):

    def test_generic(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(4.31,4.31)
        self.assertEqual("this is an example test","this is an example test")
        
        # this one is an error!
        self.assertFalse(False,"This is a custom error message blah blah blah")

    def test_my_square_root(self):
        self.assertEqual(18.0, my_square_root(324.0))
        self.assertEqual(25.4, my_square_root(645.16))
        self.assertEqual(50.332, my_square_root(2533.310224))
        self.assertEqual(0.0, my_square_root(0.0))
        self.assertEqual(-1, my_square_root(-22.0))

if __name__ == '__main__':
    unittest.main()
