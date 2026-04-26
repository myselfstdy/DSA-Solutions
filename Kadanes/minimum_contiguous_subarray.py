class Solution:
    def minimum_contiguous_subarray(self,nums):
        # Initialize variables - currsum tracks current subarray sum, minsum tracks the minimum
        currsum = nums[0]
        minsum =nums[0]
        start = temp = end = 0
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # Check if starting fresh from current element is better than extending current sum
            if nums[i] < nums[i] + currsum:
                currsum = nums[i]
                temp=i  # Mark the start of new subarray
            else:
                currsum+=nums[i]  # Extend current subarray by adding current element
            
            # Update minimum if current sum is smaller
            if currsum < minsum:
                minsum = currsum
                start = temp
                end = i 
        
        # Return the minimum sum and the subarray that produced it
        return minsum, nums[start:end+1]
        
s=Solution()
print(s.minimum_contiguous_subarray([3,3,-9,-1,1,4,-1]))
print(s.minimum_contiguous_subarray([1,2,3,5,4,5]))