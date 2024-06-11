class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for value in arr2:
            for j in range(len(arr1)):
                if arr1[j] == value:
                    result.append(arr1[j])
                    arr1[j] = -1
        arr1.sort()
        for value in arr1:
            if value != -1:
                result.append(value)
        return result
