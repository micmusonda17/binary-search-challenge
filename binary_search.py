# Binary search on a sorted list
# HyperionDev Graduate Program, Level 2 Task 8 coding challenge


def binary_search(numbers, target):
    """Return the index of target in the sorted list numbers, or -1 if it is not there."""
    low = 0
    high = len(numbers) - 1

    while low <= high:
        # check the middle item of the part of the list we are still searching
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            # the target can only be in the right half
            low = middle + 1
        else:
            # the target can only be in the left half
            high = middle - 1

    # the search space is empty, so the target is not in the list
    return -1


if __name__ == "__main__":
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("List: " + str(sorted_numbers))

    for value in [23, 2, 91, 7]:
        position = binary_search(sorted_numbers, value)
        if position == -1:
            print(str(value) + " was not found")
        else:
            print(str(value) + " found at index " + str(position))
