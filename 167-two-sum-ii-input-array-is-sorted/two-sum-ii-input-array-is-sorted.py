class Solution(object):
    def twoSum(self, numbers, target):
        result=[]
        left=0
        right= len(numbers) - 1 
        while left < right:
            value = numbers[left] + numbers [right]
            if value > target:
                right -=1
            elif value < target:
                left += 1
            else:
                result.append(left +1)
                result.append(right +1)

                left += 1
                right -= 1
        return result                
        