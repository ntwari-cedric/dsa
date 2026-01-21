class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_area=[]
        solution=0
        while left < right:
            if height[left] <= height[right]:
                solution= (right-left) * height[left]
                max_area.append(solution)
                left +=1
            else:
                solution= (right-left) * height[right]
                max_area.append(solution)
                right -=1
        return max(max_area)

        