import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../src"))

"""
# jika menggunakan class
from function_operation import functionOperation

class functionOperationTest(unittest.TestCase):
    def test_plus1Operation(self):
        actualOutput = functionOperation(2,10,'plus1').function()
        print(actualOutput)
        expectedOutput = [2,3,4,5,6,7,8,9,10]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_fibonacciOperation(self):
        actualOutput = functionOperation(2,10,'fibonacci').function()
        print(actualOutput)
        expectedOutput = [2,3,5,8]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_kuadratOperation(self):
        actualOutput = functionOperation(2,10,'kuadrat').function()
        print(actualOutput)
        expectedOutput = [2,4,8]
        self.assertEqual(actualOutput, expectedOutput)
"""

from function_operation import function

print('Is actual value equal to expected value?')

class functionOperationTest(unittest.TestCase):
    def test_plus1Operation(self):
        actualOutput = function(2,10,'plus1')
        print(actualOutput)
        expectedOutput = [2,3,4,5,6,7,8,9,10]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_fibonacciOperation(self):
        actualOutput = function(2,10,'fibonacci')
        print(actualOutput)
        expectedOutput = [2,3,5,8]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_kuadratOperation(self):
        actualOutput = function(2,10,'kuadrat')
        print(actualOutput)
        expectedOutput = [2,4,8]
        self.assertEqual(actualOutput, expectedOutput)