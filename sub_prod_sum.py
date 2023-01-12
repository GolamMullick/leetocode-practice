
import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1 = [int(x) for x in str(n)]
        sum1 = sum(list1)
        prod1 = numpy.prod(list1)
        subtraction = prod1 - sum1
        
        return subtraction
    
a = Solution()
b = a.subtractProductAndSum(4421)
print(b)
        
        















