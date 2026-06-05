class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        #this is to heap size k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)



    def add(self, val: int) -> int:
        """
            sort and position - nlogn

        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]