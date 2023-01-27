from typing import List
from collections import deque

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        st = set()
        for w in words:
            st.add(w)
        
        #check if w can be made of given words
        def check(w: str) -> bool:
            n = len(w)
            next = deque([-1])
            while next:
                start = next.pop()
                for i in range(start+1, n):
                    if w[start+1:i+1] in st or w[start+1:i+1] in found:
                        next.append(i)
                        if i == n-1:
                            return True
            return False

        #find concatenated words
        ans = []
        found = set()
        for w in words:
            st.remove(w)
            if check(w):
                ans.append(w)
                found.add(w)
            st.add(w)
        
        return ans

print(Solution().findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(Solution().findAllConcatenatedWordsInADict(words = ["cat","dog","catdog"]))