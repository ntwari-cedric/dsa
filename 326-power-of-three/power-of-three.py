class Solution(object):
    def isPowerOfThree(self, n):
        i = 0
        while i <= 32:
            if  3 **  i == n:
                return True
                break
            elif 3 ** i != 0:
                i +=1
        return False
        