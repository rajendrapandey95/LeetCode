from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Get the task with the maximum frequency
        max_count = max(task_counts.values())
        
        # Calculate the number of tasks with the maximum frequency
        num_max_tasks = sum(1 for count in task_counts.values() if count == max_count)
        
        # Calculate the number of intervals required to schedule all tasks
        # (max_count - 1) intervals are needed for each repetition of the most frequent task
        # Each interval has (n + 1) slots
        min_intervals = (max_count - 1) * (n + 1) + num_max_tasks
        
        # The result should be at least the length of the tasks array
        return max(len(tasks), min_intervals)
