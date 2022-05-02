class Balls:
    def calcDistance(self, A, B, C, D):
        return 3 * (A + B + C + D)


if __name__ == '__main__':
    print(Balls().calcDistance(100, 90, 80, 70))
