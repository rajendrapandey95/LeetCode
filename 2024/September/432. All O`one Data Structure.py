class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)  
        self.tail = Node(0) 
        self.head.next, self.tail.prev = self.tail, self.head
        self.map = {}  

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.keys.remove(key)
            new_freq = node.freq + 1
            self._move_next(node, key, new_freq)
        else:
            self._move_next(self.head, key, 1)

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        current_freq = node.freq

        if current_freq == 1:
            del self.map[key]
        else:
            new_freq = current_freq - 1
            self._move_next(node.prev, key, new_freq)

        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _move_next(self, node, key, freq):
        next_node = node.next
        if next_node == self.tail or next_node.freq != freq:
            new_node = Node(freq)
            new_node.keys.add(key)
            new_node.prev, new_node.next = node, next_node
            node.next = new_node
            next_node.prev = new_node
        else:
            next_node.keys.add(key)
            new_node = next_node

        self.map[key] = new_node

        if not node.keys and node not in [self.head, self.tail]:
            self._remove_node(node)

    def _remove_node(self, node):
        if node == self.head or node == self.tail:
            return
        node.prev.next, node.next.prev = node.next, node.prev
