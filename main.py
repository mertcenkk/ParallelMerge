import time
from mergesort.merge_sort import parallelMergeSort,mergeSort
import random

def main():
    print(time.time())
    randomlist = []
    for i in range(0, 1000000):
        n = random.randint(1, 2000000)
        randomlist.append(n)

    randforNonParallel = randomlist


    startTime = time.time()
    print("Given array is processing in serial", end="\n")
    print("wait")
    sorted = mergeSort(randforNonParallel)
    print("Array is sorted", end="\n")
    print("--- %s seconds ---" % (time.time() - startTime))

    print("-----------------------------------\n")

    startTime = time.time()
    arr = [12, 22, 14, 15, 123, 34, 45, 56, 544, 23, 34, 11, 19, 87, 33]
    print("Given array is processing in parallel")
    print("wait")
    sorted = parallelMergeSort(randomlist)
    print("Array is sorted", end="\n")
    print("--- %s seconds ---" % (time.time() - startTime))



if __name__ == '__main__':
    main()