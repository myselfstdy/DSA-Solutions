class Solution:
    def reverseArray(self, arr):
        # code here
        left =0
        right=len(arr)-1
        while left < right:
            arr[left] , arr[right] = arr[right] , arr[left]
            left+=1
            right-=1
        return arr

s=Solution()
print(s.reverseArray([1,2,3,4,5]))
print(s.reverseArray([1,2,3,4,5,6]))