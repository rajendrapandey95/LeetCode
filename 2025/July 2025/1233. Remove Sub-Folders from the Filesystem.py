class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        result = [folder[0]]

        for path in folder[1:]:
            if not path.startswith(result[-1] + '/'):
                result.append(path)

        return result
