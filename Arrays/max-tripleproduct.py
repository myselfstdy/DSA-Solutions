class Solution:
    def maxProduct(self, arr):
        # code here
        arr.sort()
        n =len(arr)
        pro1 = arr[n-1]*arr[n-2]*arr[n-3]
        pro2 = arr[0]*arr[1]*arr[n-1]
        return max(pro1,pro2)