def binary_search_recursive(phonebook, name, left, right):
    if left > right:
        return -1  
    mid = (left + right) // 2
    if phonebook[mid][0] == name:
        return mid
    elif phonebook[mid][0] < name:
        return binary_search_recursive(phonebook, name, mid + 1, right)
    else:
        return binary_search_recursive(phonebook, name, left, mid - 1)

def binary_search_iterative(phonebook, name):
    left, right = 0, len(phonebook) - 1
    while left <= right:
        mid = (left + right) // 2
        if phonebook[mid][0] == name:
            return mid
        elif phonebook[mid][0] < name:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Friend not found

def insert_friend(phonebook, name, number):
    friend = (name, number)
    index = binary_search_iterative(phonebook, name)
    if index == -1:
        # Friend not found, insert in sorted order
        for i, (existing_name, _) in enumerate(phonebook):
            if existing_name > name:
                phonebook.insert(i, friend)
                break
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
    print("2. Search for a friend (recursive)")
    print("3. Search for a friend (non-recursive)")
    print("4. Display phonebook")
    print("5. Exit")
    
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
        index = binary_search_recursive(phonebook, name, 0, len(phonebook) - 1)
        if index != -1:
            print(f"{name} found at index {index}: {phonebook[index][1]}")
        else:
            print(f"{name} not found in the phonebook.")
    elif choice == 3:
        name = input("Enter the friend's name to search: ")
        index = binary_search_iterative(phonebook, name)
        if index != -1:
            print(f"{name} found at index {index}: {phonebook[index][1]}")
        else:
            print(f"{name} not found in the phonebook.")
    elif choice == 4:
        display_phonebook(phonebook)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
