class Solution:
    def reverseingroups(self, arr, k):
        #code here
        i=0
        n=len(arr)
        while i < n:
            left = i
            right = min(k+i-1,n-1)
            while left < right :
                arr[left] , arr[right] = arr[right] , arr[left]
                left +=1
                right-=1
            i+=k
        return arr