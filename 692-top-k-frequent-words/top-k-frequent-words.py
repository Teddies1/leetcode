class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        heap = []
        ans = []
        for word, freq in hashmap.items():
            heapq.heappush(heap, (-freq, word))

        for _  in range(k):
            _, word = heapq.heappop(heap)
            ans.append(word)

        return ans