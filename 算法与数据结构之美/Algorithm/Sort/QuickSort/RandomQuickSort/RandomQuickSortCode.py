import copy
import random


def randomQuickSort(array: list):
    if len(array) < 2:
        return
    _randomQuickSort(array, 0, len(array) - 1)


def _randomQuickSort(array: list, left: int, right: int):
    if left < right:
        # less, more 分别表示与基准值相等的数列的左右边界
        less, more = partition(array, left, right, array[random.randint(left, right)])
        _randomQuickSort(array, left, less)
        _randomQuickSort(array, more, right)


def partition(array: list, left: int, right: int, pivot: int):
    """将比基准值小的数放在左边，相等的放中间，大的放右边"""
    less, more = left - 1, right + 1
    while left < more:
        if array[left] < pivot:
            less += 1
            array[left], array[less] = array[less], array[left]
            left += 1
        elif array[left] > pivot:
            more -= 1
            array[left], array[more] = array[more], array[left]
        else:
            left += 1
    return less, more


if __name__ == '__main__':
    flag = True
    for i in range(100):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        randomQuickSort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break
    print("Nice" if flag else "Fuck")
