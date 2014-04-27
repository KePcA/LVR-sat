__author__ = 'Grega'

import unittest

if __name__ == "__main__":
	"""
	Runs all of the unit tests.
	"""
	all_tests = unittest.TestLoader().discover('unit_test', pattern='*.py')
	unittest.TextTestRunner().run(all_tests)