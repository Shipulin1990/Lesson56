import unittest
import tests_12_3

tes = unittest.TestSuite()
tes.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tes.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tes)
