#sec and 1st largest
class Solution:
    def maximum_contiguous_subarray(self,nums):
        currsum = nums[0]
        maxsum =nums[0]
        start = temp = end = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + currsum:
                currsum = nums[i]
                temp=i
            else:currsum+=nums[i]
        if currsum > maxsum:
            maxsum = currsum
            start = temp
            end = i 
        return maxsum, nums[start:end+1]
        
s=Solution()
print(s.maximum_contiguous_subarray([3,3,-9,-1,1,4,-1]))
print(s.maximum_contiguous_subarray([1,2,3,-5,4,5]))