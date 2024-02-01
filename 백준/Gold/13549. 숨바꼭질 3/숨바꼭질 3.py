import heapq

N, K = map(int, input().split())

heap = [(0, N)]
heapq.heapify(heap)
distance = [int(1e9) for _ in range(100001)]
distance[N] = 0
visited = [False] * 100001
visited[N] = True
while heap:
    time, location = heapq.heappop(heap)
    visited[location] = True
    if location == K:
        print(time)
        break
    if distance[location] < time:
        continue
    if location > 0 and not visited[location-1]:
        heapq.heappush(heap, (time + 1, location - 1))
        distance[location - 1] = time + 1
    if location < 100000 and not visited[location+1]:
        heapq.heappush(heap, (time + 1, location + 1))
        distance[location + 1] = time + 1
    if 2 * location <= 100000 and not visited[location*2]:
        heapq.heappush(heap, (time, location * 2))
        distance[location * 2] = time