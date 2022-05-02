import copy
import heapq
import random


def heapInsert(arr: list, index: int):
    while arr[(index - 1) // 2] < arr[index] and index > 0:
        arr[(index - 1) // 2], arr[index] = arr[index], arr[(index - 1) // 2]
        index = (index - 1) // 2


def heapIfy(arr: list, index: int, length: int):
    left = 2 * index + 1
    while left < length:
        # 左右子节点中的最大值索引
        largest = left + 1 if (left + 1 < length) and (arr[left + 1] > arr[left]) else left
        # 节点与子节点中的最大值索引
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            # 如果节点即为最大值则无需继续调整
            break
        else:
            # 否则交换节点与最大值节点
            arr[index], arr[largest] = arr[largest], arr[index]
            index = largest
            left = 2 * index + 1


def heapSort(arr: list):
    length = len(arr)
    if length < 2:
        return
    # for index in range(1, length):
    #     heapInsert(arr, index)
    for index in range(length - 1, -1, -1):
        heapIfy(arr, index, len(arr))
    for index in range(length - 1, -1, -1):
        arr[0], arr[index] = arr[index], arr[0]
        heapIfy(arr, 0, index)


def pythonHeap(arr: list):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]


if __name__ == "__main__":
    flag = True
    for i in range(100):
        list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        heapSort(list2)
        list3 = pythonHeap(list3)
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break
    print("Nice" if flag else "Fuck")
