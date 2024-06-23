class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            ans = []
            
            for interval in intervals:
                if newInterval[0] > interval[1]:
                    ans.append(interval)
                    
            for interval in intervals:
                if interval[0] < newInterval[0]:
                    if interval[1] >= newInterval[0]:
                        newInterval[0] = interval[0]
                        
            for interval in intervals:
                if newInterval[1] < interval[1]:
                    if newInterval[1] >= interval[0]:
                        newInterval[1] = interval[1]
                        
            ans.append(newInterval)
            
            for interval in intervals:
                if interval[0] > newInterval[1]:
                    ans.append(interval)
            
            return ans