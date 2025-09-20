from collections import defaultdict, deque
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = {} 
        self.counts = defaultdict(list) 
        self.queue = deque()  

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)

        if key in self.packets:
            return False

        if len(self.packets) >= self.size:
            self.forwardPacket()

        self.packets[key] = [source, destination, timestamp]
        self.queue.append(key)

        bisect.insort(self.counts[destination], timestamp)

        return True

    def forwardPacket(self):
        if not self.packets:
            return []

        key = self.queue.popleft()
        packet = self.packets.pop(key)

        dest = packet[1]
        idx = bisect.bisect_left(self.counts[dest], packet[2])
        if idx < len(self.counts[dest]) and self.counts[dest][idx] == packet[2]:
            self.counts[dest].pop(idx)

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0

        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        return (source << 40) | (destination << 20) | timestamp
