# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

from typing import List


def largestRectangleArea(heights: List[int]):

    stack = []
    max_height = 0

    heights.append(0)

    for i in range(len(heights)):

        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            h = heights[top]

            if not stack:
                width = i
            else:
                width = i - stack[-1] -1
            
            max_height = max(max_height, h * width)
        
        stack.append(i)

    return max_height

nums = [2,1,5,6,2,3]   
print(largestRectangleArea(nums))
