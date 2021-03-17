import time


def mergeSort(arr):
    if len(arr) > 1:

        # dizinin ortasını bulur
        mid = len(arr) // 2

        # dizi elemanlarını 2 parçaya böler
        L = arr[:mid]
        print(L)
        # 2. parça
        R = arr[mid:]
        print(R)
        # ilk yarıyı sırala
        mergeSort(L)

        # ikinci yarıyı sırala
        mergeSort(R)

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
        print(arr)
        # element kalmış mı diye kontrol et
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(arr)

# listeyi print et


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    startTime = time.time()
    arr = [12,22,14,15,123,34,45,56,544,23,34,11,19,87,33]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print("--- %s seconds ---" % (time.time() - startTime))
