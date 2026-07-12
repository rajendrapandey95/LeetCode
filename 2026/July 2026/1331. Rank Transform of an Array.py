class Solution:
    def arrayRankTransform(self, arr):
        num_to_indices = {num: [] for num in sorted(set(arr))}

        for i, num in enumerate(arr):
            num_to_indices[num].append(i)

        rank = 1
        for num in num_to_indices:
            for index in num_to_indices[num]:
                arr[index] = rank
            rank += 1

        return arr
