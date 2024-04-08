from collections import deque
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Convert lists to deque for efficient popping from both ends
        students_queue = deque(students)
        sandwiches_stack = deque(sandwiches)
        
        unable_to_eat = 0
        
        while students_queue:
            if students_queue[0] == sandwiches_stack[0]:
                # Student prefers the top sandwich, they take it
                students_queue.popleft()
                sandwiches_stack.popleft()
                unable_to_eat = 0  # Reset unable_to_eat counter
            else:
                # Student doesn't prefer the top sandwich, move to the end of the queue
                students_queue.rotate(-1)
                unable_to_eat += 1
                
                # If all students rotated without taking their preferred sandwiches, break
                if unable_to_eat == len(students_queue):
                    break
        
        return len(students_queue)
