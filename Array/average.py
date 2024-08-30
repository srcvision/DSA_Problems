from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        li = 1e9
        i,j=0,len(nums)-1
        while i<=j:
            li = min(li,(nums[i]+nums[j])/2)
            print(li)
            i+=1
            j-=1
        return li      
nums=[7,8,3,4,15,13,4,1]
result = Solution()
print("Average is: ", result.minimumAverage(nums))