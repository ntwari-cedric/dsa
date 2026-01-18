class Solution:
    def targetIndices(self, nums, target):
        solution = sorted(nums)
        answer = []
        for i in range(len(solution)):
            if solution[i] == target:
                answer.append(i)
        return answer

