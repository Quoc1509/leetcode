import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: []  for i in range(n)}
        
        for from_city, to_city, price in flights:
            adj[from_city].append((to_city, price))
        queue = deque([(0, src, 0)])
        prices = [float("inf")] * n
        prices[src] = 0

        while queue:
            cost, city, stops = queue.popleft()
            if stops > k: continue
            for next_city, price in adj[city]:
                next_price = price + cost
                if next_price < prices[next_city]:
                    prices[next_city] = next_price
                    queue.append((next_price, next_city, stops + 1))
        return -1 if prices[dst] == float("inf") else prices[dst]