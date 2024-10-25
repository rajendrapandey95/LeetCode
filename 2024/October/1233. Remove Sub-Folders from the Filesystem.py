class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self):
                self.end = False
                self.children = {}

        root = TrieNode()
        for path in folder:
            node = root
            for name in path.split("/"):
                if name:
                    if name not in node.children:
                        node.children[name] = TrieNode()
                    node = node.children[name]
            node.end = True

        res = []
        for path in folder:
            node, is_sub = root, False
            for i, name in enumerate(path.split("/")):
                if name:
                    node = node.children[name]
                    if node.end and i != len(path.split("/")) - 1:
                        is_sub = True
                        break
            if not is_sub:
                res.append(path)

        return res
