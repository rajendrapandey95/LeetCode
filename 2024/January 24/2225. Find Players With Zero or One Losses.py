from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = {}

        for winner, loser in matches:
            losses_count[loser] = losses_count.get(loser, 0) + 1

        not_lost_any_matches = []
        lost_one_match = []

        for player in set(player for match in matches for player in match):
            if player not in losses_count:
                not_lost_any_matches.append(player)
            elif losses_count[player] == 1:
                lost_one_match.append(player)

        not_lost_any_matches.sort()
        lost_one_match.sort()

        return [not_lost_any_matches, lost_one_match]

