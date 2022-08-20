import Code_coverage.mymath as mymath
import unittest


class TestAdd(unittest.TestCase):
    '''
    Test add funstion from mymath
    '''
    def test_add_integer(self):
        '''
        Tset add of two integer returns of the correct total
        '''

    result = mymath.add(10, 5)
    self.assertEgual(result, 15)

if __name__ =='__main__':
    unittest.main()