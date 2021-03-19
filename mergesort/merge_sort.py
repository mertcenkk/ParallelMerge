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


def parallelMergeSort(arr,cpu_count=multiprocessing.cpu_count()): #cpu count özel olarak girilmediği sürece default olarak sistemden işlemci sayısını alır.
    if cpu_count>1 : #işlemci sayısı 1'e ininceye kadar çalıştır
        cpu_count=cpu_count//2  #işlemci sayısını yarıya indir. (Her pool'a 2 işlemci gidiyor) Kaç defa daha girebileceğini belirler
        # örneğin işlemci sayısı 16 ise 2 üzeri 4ten 4 defa girebilir 4 birimlik derinliğe ulaşırken 16 process çalıştırır.
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        full = [left, right] # pool iterable değer beklediği için sol ve sağ listeyi ayrı bir liste ekliyoruz.
        parallelMergeSort(left,cpu_count)
        parallelMergeSort(right,cpu_count)
        pool = multiprocessing.Pool(processes=2)
        result = pool.map(mergeSort, full)  #iterable bekliyor

        pool.close()
        pool.join()
        return merge(result[0],result[1],arr) #birleştirmeye gönderilmek üzere result listesinden left ve right listeleri seçilir.






