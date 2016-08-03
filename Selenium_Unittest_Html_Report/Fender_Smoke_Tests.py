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

# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=outfile,
                 title='Test Report',
                 description='Smoke Tests'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)

