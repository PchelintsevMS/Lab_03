def bubble_sort(arr, ascending=True):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ascending:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input("Введите количество чисел: "))
numbers = []
for _ in range(n):
    num = float(input("Введите число: "))
    numbers.append(num)
direction = input("Выберите направление сортировки (asc/desc): ").lower()
bubble_sort(numbers, ascending=direction == "asc")
print("Отсортированный список:", numbers)
