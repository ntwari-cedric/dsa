class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right= len(skill) -1
        chemistry=0
        target = skill[left] + skill[right]
        while left < right:
            if target == skill[left] + skill[right]:
                chemistry += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return chemistry
        