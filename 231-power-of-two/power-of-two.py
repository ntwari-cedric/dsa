class Solution(object):
    def isPowerOfTwo(self, n):
        i = 0
        while i <= 32:
            if  2 **  i == n:
                return True
                break
            elif 2 ** i != 0:
                i +=1
        return False