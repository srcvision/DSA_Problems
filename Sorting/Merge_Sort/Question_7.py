# Quesion-7
# Minimum Sum of Four Digit Number After Splitting Digits Using Merge Sort
class Solution:
    def minimumSum(self, num: int) -> int:
        def merger_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left = merger_sort(arr[:mid])
            right=merger_sort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            new = []
            i = j = 0
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
        def duplicate(num):
            digits = [int(d) for d in str(num)]
            pairs = []
            for i in range(1,len(digits)):
                num1 = int(''.join(map(str,digits[:i])))
                num2 = int(''.join(map(str,digits[i:])))
                pairs.append(num1+num2)
            merger_sort(pairs)
            return pairs[0]
        return duplicate(num)
selection = Solution()
num = 2932
num = selection.minimumSum(num)

print("Minimum Sum of Four Digit Number After Splitting Digits is:",num)

        
