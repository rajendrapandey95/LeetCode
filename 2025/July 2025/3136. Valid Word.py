class Solution:
    def isValid(self, w: str) -> bool:
        if len(w) < 3: return False
        v, c = False, False
        for ch in w:
            if ch.isalpha():
                (v, c)[ch.lower() not in 'aeiou'] = True
            elif not ch.isdigit():
                return False
        return v and c
