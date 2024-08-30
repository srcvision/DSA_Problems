# Quesion-4
from typing import List
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        def selecton_sort(arr):
            n = len(arr)
            for i in range(n-1):
                mini = i
                for j in range(i+1,n):
                    if arr[mini]<arr[j]:
                        mini = j
                    arr[i],arr[mini]=arr[i],arr[mini]
                
        n = len(nums)
        result = selecton_sort(nums)
        ans = 0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                ans+=i+1
        return ans
solution = Solution()
nums = [5, 1, 3, 2]
print(solution.reductionOperations(nums))
