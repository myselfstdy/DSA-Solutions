class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        #arr.sort()
        lar=sec=0
        for i in arr:
            if i > lar:
                sec=lar
                lar = i
            elif sec < i and i!=lar:
                sec=i
        if len(set(arr)) < 2:
            return -1
        return sec
s = Solution()
print(s.getSecondLargest([1, 2, 3, 4, 5]))
print(s.getSecondLargest([1, 1, 1, 1, 1]))