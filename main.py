def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Введите количество чисел: "))
numbers = []
for _ in range(n):
    num = float(input("Введите число: "))
    numbers.append(num)
bubble_sort(numbers)
print("Отсортированный список:", numbers)
