class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        for string_index in range(len(s)):
            if space_index < len(spaces) and string_index == spaces[space_index]:
                result.append(" ")
                space_index += 1
            result.append(s[string_index])
        return "".join(result)
