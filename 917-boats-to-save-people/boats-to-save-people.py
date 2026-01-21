class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        count = 0
        right = len(people) -1
        left= 0
        while right >= left:
            if people[right] + people[left] <= limit:
                count += 1
                right -= 1
                left += 1
            else:
                count +=1
                right -=1

        return count
        