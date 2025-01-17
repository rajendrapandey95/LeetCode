class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def validate(start):
            original = [start]
            for num in derived:
                original.append(num ^ original[-1])
            return original[0] == original[-1]

        return validate(0) or validate(1)
