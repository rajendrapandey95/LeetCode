from collections import Counter
from math import ceil

class Solution(object):
    def numRabbits(self, answers):
        mpp = Counter(answers)
        total = 0

        for x in mpp:
            group_size = x + 1 
            num_groups = ceil(mpp[x] / float(group_size))  
            total += num_groups * group_size 

        return int(total)
