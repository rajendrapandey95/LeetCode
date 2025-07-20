from typing import List
from collections import Counter

class Trie:
    def __init__(self):
        self.children = dict()
        self.serial = ""

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        for path in paths:
            cur = root
            for folder in path:
                if folder not in cur.children:
                    cur.children[folder] = Trie()
                cur = cur.children[folder]

        freq = Counter()

        def serialize(node: Trie) -> str:
            if not node.children:
                return ""
            serials = []
            for folder, child in node.children.items():
                child_serial = serialize(child)
                serials.append(folder + "(" + child_serial + ")")
            serials.sort()
            node.serial = "".join(serials)
            freq[node.serial] += 1
            return node.serial

        serialize(root)

        def remove_duplicates(node: Trie):
            keys_to_delete = [k for k, child in node.children.items() if freq[child.serial] > 1]
            for k in keys_to_delete:
                del node.children[k]
            # Recurse into remaining children
            for child in node.children.values():
                remove_duplicates(child)

        remove_duplicates(root)

        result = []
        path = []

        def collect(node: Trie):
            for folder, child in node.children.items():
                path.append(folder)
                result.append(path[:])
                collect(child)
                path.pop()

        collect(root)
        return result
