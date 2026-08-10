class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        result=0
        while left < right:
            distance=right-left
            m=min(height[left],height[right])
            final=distance*m
            if final>result:
                result=final
            elif height[left]<height[right]:
                left+=1
            else:
                right-=1
            
        return result             
        