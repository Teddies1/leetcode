class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        occurence_map = {}
        left, n = 0, len(cards)
        num_cards = float("inf")

        for right in range(n):
            if cards[right] not in occurence_map:
                occurence_map[cards[right]] = 1
            else:
                occurence_map[cards[right]] += 1

            while occurence_map[cards[right]] > 1:
                length = right - left + 1
                num_cards = min(num_cards, length)
                occurence_map[cards[left]] -= 1
                left += 1
            
        return num_cards if num_cards != float("inf") else -1