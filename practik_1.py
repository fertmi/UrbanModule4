nums = [7, 8, 2, 4, 6, 1, 3]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls)-1):
            if ls[i] > ls [i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True

# bubble_sort(nums)
# print(nums)

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]

selection_sort(nums)
print(nums)