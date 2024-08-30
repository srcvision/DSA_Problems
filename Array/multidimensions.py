from typing import List
import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal=0
        max_area = 0
        for l,w in dimensions:
            diagonal=math.sqrt(l**2+w**2)
            if diagonal > max_diagonal:
                max_diagonal=diagonal
                max_area=l*w
            elif diagonal==max_diagonal:
                max_area = max(max_area,l*w)
        return max_area

dimensions = [[9,3],[8,6]]
result = Solution()
print("Area of max diagonal is: ", result.areaOfMaxDiagonal(dimensions))