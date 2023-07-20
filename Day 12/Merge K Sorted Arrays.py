import heapq
def mergeKSortedArrays(kArrays, k:int):
    heap=[]
    final=[]
    for i in range(len(kArrays)):
        heapq.heappush(heap,(kArrays[i][0],i,0))
    while heap:
        ele,aIndex,eleIndex=heapq.heappop(heap)
        final.append(ele)
        if eleIndex+1<len(kArrays[aIndex]):
            heapq.heappush(heap,(kArrays[aIndex][eleIndex+1],aIndex,eleIndex+1))
    return final