class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = [0] * (n+1)
        return self.recurse(questions, cache, 0)

    def recurse(self, questions, cache, index):
        n = len(questions)
        if index >= n:
            return 0
        if index == n-1:
            return max(questions[n-1][0], 0)
        
        if cache[index] != 0:
            return cache[index]

        score =  questions[index][0]
        brainpower = questions[index][1]

        if (index + brainpower + 1) < n and (index + 1) < n:
            take_question = score + self.recurse(questions, cache, brainpower + index + 1)
            skip_question = self.recurse(questions, cache, index + 1)
            
            cache[index] = max(take_question, skip_question)

            return cache[index]
        else:
            cache[index] = max(score, self.recurse(questions, cache, index+1))

            return cache[index]