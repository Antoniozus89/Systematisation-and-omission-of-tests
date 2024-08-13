import unittest
from Module12.HW3 import TR_test
import r_test

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(r_test.RunnerTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TR_test.TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

