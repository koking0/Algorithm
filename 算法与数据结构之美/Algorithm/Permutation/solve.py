def permutation(arr, left, right):
    if left > right - 1:
        print(arr)
    for i in range(left, right):
        arr[left], arr[i] = arr[i], arr[left]
        permutation(arr, left + 1, right)
        arr[left], arr[i] = arr[i], arr[left]


if __name__ == '__main__':
    nums = [1, 2, 3]
    permutation(nums, 0, len(nums))
