def hanoi(n, start, helper, target):
    """
    :param n: 表示盘子的个数
    :param start: 表示起始柱子
    :param helper: 表示辅助柱子
    :param target: 表示目标柱子
    """
    if n > 0:
        hanoi(n - 1, start, target, helper)
        print(f"Move {n} from {start} to {target}")
        hanoi(n - 1, helper, start, target)


if __name__ == '__main__':
    hanoi(3, "A", "B", "C")
