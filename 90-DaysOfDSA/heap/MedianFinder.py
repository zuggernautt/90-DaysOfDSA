class MedianFinder:

    def __init__(self):
        self.small =[]
        self.large=[]
        
    import heapq
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)
        # every ele in small is <= every ele of large
        if  self.small and self.large and -1*self.small[0]>self.large[0]:
            val=-1*self.heapq.heappop(self.small)
            self.heapq.heappush(self.large, val)

        #difference in lengths in heaps is !> 1
        if len(self.small)>len(self.large)+1:
            val=-1*self.heapq.heappop(self.small)
            self.heapq.heappush(self.large, val)
        if len(self.large)>len(self.small):
            val=self.heapq.heappop(self.large)
            self.heapq.heappush(self.small,-1* val)



        
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return (-1*self.small[0]+self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()