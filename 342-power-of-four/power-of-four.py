class Solution(object):
    def isPowerOfFour(self, n):
        i = 0
        while i <= 32:
            if  4 **  i == n:
                return True
                break
            elif 4 ** i != 0:
                i +=1
        return False
        