import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

# def solution(food_times, k):
#     answer = -1
#     sec = 0
#     index = 0
#
#     if sum(food_times) <= k:
#         return -1
#
#     while True:
#         if sec >= k:
#             break
#
#         if food_times[index % 3] == 0:
#             index += 1
#             continue;
#         else:
#             food_times[index % 3] -= 1
#             sec += 1
#             index += 1
#
#     return index % 3 + 1
