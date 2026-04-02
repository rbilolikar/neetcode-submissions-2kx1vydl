class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    water += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    water += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return water

        


