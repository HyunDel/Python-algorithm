import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = collections.Counter(nums)
        freqs_heap = []
        
        for f in freq :
            heapq.heappush(freqs_heap,(-freq[f],f))
            
        topk = []
        
        for i in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            
        return topk
        
        