class MedianFinder:

    def __init__(self):
        self.left_heap = [] #max heap
        self.right_heap = [] #min heap
        

    def addNum(self, num: int) -> None:
        if not self.left_heap or  num < -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)

            #rebalance the queue
            if(len(self.left_heap) > len(self.right_heap) + 1):
                heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        else:
            heapq.heappush(self.right_heap, num)

             #rebalance the queue
            if(len(self.right_heap) > len(self.left_heap)):
                heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))


    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0])/2
        else:
            return -self.left_heap[0]
        
        