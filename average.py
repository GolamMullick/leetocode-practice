from ast import List


class Solution:
    def average(self, salary):
        return ((sum(salary)- max(salary) - min(salary))/ (len(salary)-2) )
            
a = Solution()
b = a.average([1,2,3,4])
print(b)