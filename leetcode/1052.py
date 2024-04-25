from typing import List
from collections import deque

class LimitQueue:
    def __init__(self, limit):
        self.limit = limit
        self.value = 0
        self.data = deque(maxlen=limit)

    def add(self, v):
        if self.data.__len__() == self.limit:
            self.value -= self.data.popleft()
        self.data.append(v)
        self.value += v
        return self.value

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        raw = sum([customers[j] * (1 - grumpy[j]) for j in range(len(customers))]) # 10 个 , n
        # print(raw)
        mx = 0 # 最大挽留人数
        lq = LimitQueue(minutes)
        for i in range(len(customers)):
            # print(i, i + minutes)
            customer = lq.add(customers[i] * grumpy[i])
            mx = max(mx, customer)

        return mx + raw


if __name__ == '__main__':
    print(Solution().maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3))