class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        not_in_arr2=[]
        in_arr2=[]
        answer=[]
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                not_in_arr2.append(arr1[i])
            else:
                in_arr2.append(arr1[i])
        not_in_arr2.sort()
        count= Counter(in_arr2)
        print(count)
        for num in arr2:
            answer.extend([num] * count[num])
        return answer + not_in_arr2
        