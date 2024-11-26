import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def ukur_waktu(sort_function, data):
    mulai = time.time()
    sort_function(data)
    selesai = time.time()
    return selesai - mulai

if __name__ == "__main__":
    random.seed(40)
    data = [random.randint(0, 100) for _ in range(50)]
    print("Data sebelum diurutkan:", data)

    data_bubble = data.copy()
    waktu_bubble = ukur_waktu(bubble_sort, data_bubble)
    print("\nData setelah diurutkan (Bubble Sort):", data_bubble)
    print("Waktu eksekusi Bubble Sort:", waktu_bubble, "detik")

    data_merge = data.copy()
    waktu_merge = ukur_waktu(merge_sort, data_merge)
    print("\nData setelah diurutkan (Merge Sort):", data_merge)
    print("Waktu eksekusi Merge Sort:", waktu_merge, "detik")

    best_case = sorted(data)
    waktu_bubble_best = ukur_waktu(bubble_sort, best_case)
    waktu_merge_best = ukur_waktu(merge_sort, best_case)
    print("\nWaktu eksekusi Bubble Sort (Best Case):", waktu_bubble_best, "detik")
    print("Waktu eksekusi Merge Sort (Best Case):", waktu_merge_best, "detik")
