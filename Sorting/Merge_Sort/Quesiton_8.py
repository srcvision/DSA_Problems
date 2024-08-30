# Quesion-3
# The Quesion are Merge Sort but i Will be using the Selection sort algorithm

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two 
# integers m and n,representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored
# inside the array nums1. To accommodate this, nums1 has a length of 
# m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Solution:
    def merge(self, nums1: int, m: int, nums2: int, n: int) -> None:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            new = []
            i,j = 0,0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    new.append(left[i])
                    i+=1
                else:
                    new.append(right[j])
                    j+=1
            new.extend(left[i:])
            new.extend(right[j:])
            return new
        for j in range(n):
            nums1[m+j]=nums2[j]
        return merge_sort(nums1)
solution = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
solution.merge(nums1, m, nums2, n)
print("Anwser is:",nums1)
