class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if s1 == s2:
            return True
        if len(s2) < len(s1):
            return False
        
        dict1, dict2 = {}, {}
        for i in range(len(s1)):
            if s1[i] not in dict1:
                dict1[s1[i]] = 1
            else: 
                dict1[s1[i]] += 1
        for i in range(len(s1)):
            if s2[i] not in dict2:
                dict2[s2[i]] = 1
            else:
                dict2[s2[i]] += 1 
                
        left = 0
        for right in range(k, len(s2)):
            if dict1 == dict2:
                return True
            
            word = s2[left]
            if word in dict2:
                if dict2[word] > 1:
                    dict2[word] -= 1
                else:
                    dict2.pop(word)
             
            word = s2[right]
            if word not in dict2:
                dict2[word] = 1
            else: 
                dict2[word] += 1 
            left += 1
        
        return dict1 == dict2