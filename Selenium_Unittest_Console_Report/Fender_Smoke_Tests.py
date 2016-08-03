import unittest
import HTMLTestRunner
#Download HTML testrunner from http://tungwaiyip.info/software/HTMLTestRunner.html
import os
from Fender_Challenge_buy_guitar_tests import BuyGuitarTests

# get the directory path to output report file
dir = os.getcwd()

#get all tests from BuyGuitarTests class
buy_guitar_tests= unittest.TestLoader().loadTestsFromTestCase(BuyGuitarTests)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([buy_guitar_tests])

#run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)

