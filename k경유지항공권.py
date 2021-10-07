from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u,v,w in flights :
            graph[u].append((v,w))
            
        Q =[(0,src,k)]
        
        while Q :
            price, node, z = heapq.heappop(Q)
            if node == dst :
                return price 
            if z >= 0:
                for v , w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q,(alt,v,z-1))
        return -1