import heapq

class MedianFinder:
    def __init__(self):
        self.maxheap = []  # lower half (as max-heap using negatives)
        self.minheap = []  # upper half

    def addNum(self, num: int) -> None:
        # Always push to maxheap first
        heapq.heappush(self.maxheap, -num)

        # Move the largest from maxheap to minheap
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        # Balance heaps: maxheap can have at most 1 more element
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2


# -------------------------------
# ✅ Test cases
# -------------------------------
if __name__ == "__main__":
    mf = MedianFinder()

    nums = [1, 2, 3, 4, 5, 6]
    print("Adding numbers:", nums)
    for n in nums:
        mf.addNum(n)
        print(f"After adding {n}, median = {mf.findMedian()}")

    print("\nAnother test:")
    mf2 = MedianFinder()
    stream = [5, 15, 1, 3]
    for n in stream:
        mf2.addNum(n)
        print(f"Added {n}, current median = {mf2.findMedian()}")
