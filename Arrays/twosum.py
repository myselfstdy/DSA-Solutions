class Solution:
	def twoSum(self, arr, target):
		# code here
		s = set()
		for num in arr:
		    need = target - num
		    if need in s:
		        return True
		    s.add(num)
		return False
		    
		    
		'''n =len(arr)
		for i in range(n):
		    for j in range(i+1,n):
		        if arr[i]+arr[j]==target:
		            return True
        return False'''
