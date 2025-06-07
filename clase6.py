import random

def linear_search(list, objetive):
    match = False
    for element in list:
        if element == objetive:
            match = True
            break

    return match

if __name__ == "__main__":
    list_length = int(input("Enter the length of the list: "))
    objetive = int(input("Enter the objective number: "))

    list = [random.randint(0, 100) for _ in range(list_length)]
    found = linear_search(list, objetive)

    print("List:", list)
    print(f'the element {objetive} {"is" if (found) else "is not"} in the list.')
