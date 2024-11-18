import time

# Kelas untuk merepresentasikan Array
class ArraySorter:
    def __init__(self, nama, data):
        self.nama = nama
        self.data_asli = data
        self.data_terurut = None

    def bubble_sort(self):
        data = self.data_asli.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        self.data_terurut = data
        return data

    def quick_sort(self, arr=None, low=0, high=None):
        if arr is None:
            arr = self.data_asli.copy()
            high = len(arr) - 1

        if low < high:
            pi = self._partisi(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

        self.data_terurut = arr
        return arr

    def _partisi(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def ukur_waktu_sort(self, metode):
        start_time = time.time()
        if metode == "bubble_sort":
            self.bubble_sort()
        elif metode == "quick_sort":
            self.quick_sort()
        end_time = time.time()
        return end_time - start_time


# Menentukan algoritma yang lebih efektif
def tentukan_algoritma_terbaik(array_sorter, nama_array):
    waktu_bubble = array_sorter.ukur_waktu_sort("bubble_sort")
    waktu_quick = array_sorter.ukur_waktu_sort("quick_sort")

    if waktu_bubble < waktu_quick:
        algoritma_terbaik = "Bubble Sort"
        waktu_terbaik = waktu_bubble
    else:
        algoritma_terbaik = "Quick Sort"
        waktu_terbaik = waktu_quick

    print(f"Hasil untuk Array {nama_array}:")
    print(f"Algoritma yang lebih efektif: {algoritma_terbaik}")
    print(f"Waktu eksekusi: {waktu_terbaik:.6f} detik\n")


# Membuat objek untuk A dan B
array_a = ArraySorter("A", [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
array_b = ArraySorter("B", [0, 1, 2, 3, 4, 8, 8, 7, 6, 5])

# Menampilkan hasil sorting dan waktu eksekusi untuk Array A dan B
print(f"Hasil untuk Array {array_a.nama}:")
print(f"Data Asli: {array_a.data_asli}")
print(f"Waktu Bubble Sort: {array_a.ukur_waktu_sort('bubble_sort'):.6f} detik")
print(f"Waktu Quick Sort: {array_a.ukur_waktu_sort('quick_sort'):.6f} detik\n")

print(f"Hasil untuk Array {array_b.nama}:")
print(f"Data Asli: {array_b.data_asli}")
print(f"Waktu Bubble Sort: {array_b.ukur_waktu_sort('bubble_sort'):.6f} detik")
print(f"Waktu Quick Sort: {array_b.ukur_waktu_sort('quick_sort'):.6f} detik\n")

# Menentukan algoritma yang lebih efektif untuk Array A dan B
tentukan_algoritma_terbaik(array_a, "A")
tentukan_algoritma_terbaik(array_b, "B")
