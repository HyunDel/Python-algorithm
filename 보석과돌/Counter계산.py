import collections
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count =0 
        
        for char in jewels :
            count += freqs[char]
            
        return count 