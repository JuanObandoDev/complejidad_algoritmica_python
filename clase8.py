import random

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

if __name__ == "__main__":
    list_length = int(input("Enter the length of the list: "))
    list = [random.randint(0, 100) for _ in range(list_length)]
    print("List:", bubble_sort(list))
