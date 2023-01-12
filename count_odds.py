class Solution:
  def countOdds(self, low: int, high: int) -> int:
      count = 0
      for i in range(low, high+1):
          if i%2 != 0:
              count += 1
          else:
              continue
      return count
       
a = Solution()
b = a.countOdds(1,7)

print(b)