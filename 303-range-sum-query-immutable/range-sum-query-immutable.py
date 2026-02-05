class NumArray:

    def __init__(self, nums: List[int]):
        n= len(nums)
        self.answer= [0] * n
        self.answer[0]= nums[0]
        for i in range(1,n):
            self.answer[i]= self.answer[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
           solution= self.answer[right]
        else:
            solution= self.answer[right]- self.answer[left-1]
        return solution
        

