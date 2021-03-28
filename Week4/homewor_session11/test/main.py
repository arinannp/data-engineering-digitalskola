import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../src"))

"""  
# jika menggunakan class  
from function_operation import functionOperation
 
data1 = functionOperation(2,10,'plus1').function()
data2 = functionOperation(2,10,'fibonacci').function()
data3 = functionOperation(2,10,'kuadrat').function()
data4 = functionOperation(2,10,'select-operation').function()

print(data1)
print(data2)
print(data3)
print(data4)
"""

from function_operation import function
 
data1 = function(2,10,'plus1')
data2 = function(2,10,'fibonacci')
data3 = function(2,10,'kuadrat')
data4 = function(2,10,'select-operation')

print(data1)
print(data2)
print(data3)
print(data4)