class Solution:
    def judgeCircle(self, s):
        return s.count('U')==s.count('D') and s.count('L')==s.count('R')
    
