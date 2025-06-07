import random

def binary_search(list, start, end, objetive):
    if start > end:
        return False
    
    mid = (start + end) // 2
    if list[mid] == objetive:
        return True
    elif list[mid] < objetive:
        return binary_search(list, mid + 1, end, objetive)
    else:
        return binary_search(list, start, mid - 1, objetive)

if __name__ == "__main__":
    list_length = int(input("Enter the length of the list: "))
    objetive = int(input("Enter the objective number: "))

    list = sorted([random.randint(0, 100) for _ in range(list_length)])
    found = binary_search(list, 0, len(list), objetive)

    print("List:", list)
    print(f'the element {objetive} {"is" if (found) else "is not"} in the list.')
