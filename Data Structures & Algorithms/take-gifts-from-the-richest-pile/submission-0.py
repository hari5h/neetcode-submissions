class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        heap solution
        max heap
        max num --> 4

        """

        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        res = 0

        while k:
            maxGiftPile = -heapq.heappop(gifts)
            reducedPile = floor(sqrt(maxGiftPile))
            heapq.heappush(gifts,-reducedPile)
            k -=1

        return abs(sum(gifts))
