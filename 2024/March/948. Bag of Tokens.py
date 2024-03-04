class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # Sort the tokens to use them optimally
        
        left, right = 0, len(tokens) - 1  # Pointers for the leftmost and rightmost elements
        score = 0  # Initialize score
        max_score = 0  # Initialize maximum score
        
        while left <= right:
            if power >= tokens[left]:  # If we can play face-up
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:  # If we can play face-down and have some score
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break  # If neither face-up nor face-down moves are possible, break
        
        return max_score
