class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size, current = 0, head
        while current:
            size += 1
            current = current.next
        
        split_size, extra = divmod(size, k)
        
        result = []
        current = head
        for i in range(k):
            part_head = current
            for j in range(split_size + (i < extra) - 1):
                if current:
                    current = current.next
            
            if current:
                temp, current.next = current.next, None
                current = temp
            
            result.append(part_head)
        
        return result
