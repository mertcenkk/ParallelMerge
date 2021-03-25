import concurrent.futures
import math
import multiprocessing
from concurrent import futures
import time



def merge(L,R):
    arr = arrFiller(L,R)
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
        return merge(L,R)

    else:
        return arr


def parallelMergeSort(arr,cpu_count=multiprocessing.cpu_count()): #cpu count özel olarak girilmediği sürece default olarak sistemden işlemci sayısını alır.

#işlemci sayısı 1'e ininceye kadar çalıştır
#işlemci sayısını yarıya indir. (Her pool'a 2 işlemci gidiyor) Kaç defa daha girebileceğini belirler
# örneğin işlemci sayısı 16 ise 2 üzeri 4ten 4 defa girebilir 4 birimlik derinliğe ulaşırken 16 process çalıştırır.
# pool iterable değer beklediği için sol ve sağ listeyi ayrı bir liste ekliyoruz.
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        full = [left, right]
        if cpu_count == 1:
            l = mergeSort(left)
            r = mergeSort(right)
            return merge(l,r)

        else:
            result = []
            with futures.ProcessPoolExecutor(cpu_count) as p:
                cpu_count = cpu_count // 2
                if cpu_count > 0:

                    cpu_countlist = [cpu_count,cpu_count]
                    future = p.map(parallelMergeSort,full,cpu_countlist)
                    for value in future:
                        result.append(value)
            return merge(result[0],result[1])

def arrFiller(l,r):
    arr=[]
    for i in range(0,len(l)+len(r)):
        arr.append(0)
    return arr


