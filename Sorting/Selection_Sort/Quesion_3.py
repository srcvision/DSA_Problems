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
        def selection_sort(arr):
            n=len(arr)
            for i in range(n-1):
                mini =i
                for j in range(i+1,n):
                    if arr[j]<arr[mini]:
                        mini=j
                        arr[i],arr[mini]=arr[mini],arr[i]
            return arr
        for j in range(n):
            nums1[m+j]=nums2[j]
        return selection_sort(nums1)
solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution.merge(nums1, m, nums2, n)
print("Anwser is:",nums1)
