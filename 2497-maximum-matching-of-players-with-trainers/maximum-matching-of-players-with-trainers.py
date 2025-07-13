class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        matchings = 0
        n, m = len(players), len(trainers)
        players.sort()
        trainers.sort()

        player_pointer, trainer_pointer = 0, 0
        while player_pointer < n and trainer_pointer < m:
            if players[player_pointer] <= trainers[trainer_pointer]:
                matchings += 1
                player_pointer += 1
                trainer_pointer += 1
            elif players[player_pointer] > trainers[trainer_pointer]:
                trainer_pointer += 1
            
        return matchings