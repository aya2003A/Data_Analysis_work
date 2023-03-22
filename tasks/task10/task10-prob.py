class Solution(object):
    def trap(self, height):
        left=0
        right =len(height)-1
        count = 0
        maxLeft=0
        maxRight = 0 
        while left < right:
             if height[left] <= height[right]:
                 count += max(0, maxLeft - height[left])
                 maxLeft = max(maxLeft, height[left])
                 left += 1
             else:
                 count += max(0, maxRight - height[right])
                 maxRight = max(maxRight, height[right])
                 right -= 1
    
        return count  