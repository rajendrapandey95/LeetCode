from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition_sizes = []
        last_occurrence = [0] * 26  
        partition_start, partition_end = 0, 0

        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        for i, char in enumerate(s):
            partition_end = max(partition_end, last_occurrence[ord(char) - ord("a")])

            if i == partition_end:
                partition_sizes.append(partition_end - partition_start + 1)
                partition_start = i + 1  

        return partition_sizes
