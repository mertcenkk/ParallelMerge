import concurrent.futures
import math
import multiprocessing
from multiprocessing import Pool
import time


def merge(L,R,arr):
    i = j = k = 0

    # veriyi l ve r adında geçici listelere kopyala
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # element kalmış mı diye kontrol et
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr


def mergeSort(arr):

    if len(arr) > 1:

        # dizinin ortasını bulur
        mid = len(arr) // 2

        # dizi elemanlarını 2 parçaya böler
        L = arr[:mid]
        #print(L)
        # 2. parça
        R = arr[mid:]
        #print(R)
        # ilk yarıyı sırala
        mergeSort(L)

        # ikinci yarıyı sırala
        mergeSort(R)
        return merge(L,R,arr)

    else:
        return arr


# listeyi print et
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()



def parallelMergeSort(arr):
    # processes = multiprocessing.cpu_count()
    # pool = multiprocessing.Pool(processes=2)
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    full = [left, right]
    pool = multiprocessing.Pool(processes=2)
    result = pool.map(mergeSort, full)
    print(result)

    pool.close()
    pool.join()
    return merge(result[0],result[1],arr)
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     f1 = executor.submit(mergeSort, (left, ))
    #     f2 = executor.submit(mergeSort, (right, ))
    #     f1.done()
    #     f2.done()
    #     result_left = f1.result()
    #     result_right = f2.result()
    #     print(result_left)
    #     print(result_right)
if __name__ == '__main__':
    startTime = time.time()
    arr = [12, 22, 14, 15, 123, 34, 45, 56, 544, 23, 34, 11, 19, 87, 33]
    print(arr)
    print("Given array is", end="\n")
    printList(arr)
    sorted = parallelMergeSort(arr)
    print("Sorted array is: ", end="\n")
    print(sorted)
    print("--- %s seconds ---" % (time.time() - startTime))




