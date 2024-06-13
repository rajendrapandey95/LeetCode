class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_position = max(max(seats), max(students))
        differences = [0] * max_position
        
        for position in seats:
            differences[position - 1] += 1
            
        for position in students:
            differences[position - 1] -= 1
            
        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference
            
        return moves
