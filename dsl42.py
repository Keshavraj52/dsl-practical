


def fibonacci_search(phonebook, name):
    def find_fibonacci_numbers(n):
        fib_numbers = [0, 1]
        while fib_numbers[-1] < n:
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers

    def search_fibonacci(fib_numbers, phonebook, name):
        offset = -1
        while fib_numbers[-1] > 1:
            i = min(offset + fib_numbers[-2], len(phonebook) - 1)
            if phonebook[i][0] < name:
                fib_numbers = fib_numbers[:-1]
                offset = i
            elif phonebook[i][0] > name:
                fib_numbers = fib_numbers[:-2]
            else:
                return i
        if len(phonebook) > 0 and phonebook[offset + 1][0] == name:
            return offset + 1
        return -1

    fib_numbers = find_fibonacci_numbers(len(phonebook))
    index = search_fibonacci(fib_numbers, phonebook, name)
    return index

def insert_friend(phonebook, name, number):
    friend = (name, number)
    index = fibonacci_search(phonebook, name)
    if index == -1:
        # Friend not found, insert in sorted order
        for i, (existing_name, _) in enumerate(phonebook):
            if existing_name > name:
                phonebook.insert(i, friend)
                return True
        else:
            # Friend should be inserted at the end
            phonebook.append(friend)
            return True
    else:
        # Friend already exists
        return False

def display_phonebook(phonebook):
    for name, number in phonebook:
        print(f"{name}: {number}")

phonebook = []
while True:
    print("1. Add a friend")
    print("2. Search for a friend (Fibonacci search)")
    print("3. Display phonebook")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the friend's name: ")
        number = input("Enter the friend's mobile number: ")
        if insert_friend(phonebook, name, number):
            print("Friend added to the phonebook.")
        else:
            print("Friend already exists in the phonebook.")
    elif choice == 2:
        name = input("Enter the friend's name to search: ")
        index = fibonacci_search(phonebook, name)
        if index != -1:
            print(f"{name} found at index {index}: {phonebook[index][1]}")
        else:
            print(f"{name} not found in the phonebook.")
    elif choice == 3:
        display_phonebook(phonebook)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")