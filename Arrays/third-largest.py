#third largest element in an array
class Solution:
    def thirdlargest(self,nums):
        n = len(nums)
        if n < 3:
            return -1
        nums.sort()
        return nums[n-3]
        
s=Solution()
print(s.thirdlargest([3,3]))
print(s.thirdlargest([1,2,3,4,5]))