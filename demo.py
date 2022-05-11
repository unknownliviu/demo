#some change on master
def search(arr, looking_for):
    if looking_for < arr[0] or looking_for > arr[-1]:
        return -1
    lindex = 0
    rindex = len(arr) - 1
    while lindex <= rindex:
        mid = (lindex + rindex) // 2
        if arr[mid] == looking_for:
            return mid
        if looking_for > arr[mid]:
            lindex = mid + 1
        else:
            rindex = mid - 1
    return -1


def find_index(list, start, finish, number):
    if list[finish - 1] < number or list[start] > number:
        print("-1")
    else:
        mid = (start + finish) // 2
        if number == list[mid]:
            print(mid)
        elif number < list[mid]:
            find_index(list, start, mid, number)
        else:
            find_index(list, mid + 1, finish, number)


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    looking_for = int(lines[0].strip())

    arr = [int(x) for x in lines[1].split(" ")]
    print(looking_for, arr)
    # return search(arr, looking_for)
    return find_index(arr, 0, len(arr), looking_for)


# print(main())

print("somedata")