# check if given list of integers contains duplicates

hashset = set()


def duplicates(arr):
    for num in arr:
        if num in hashset:
            return True
        hashset.add(num)
    return False
