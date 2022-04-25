class Apples:
    def getInitial(self, n):
        m = 1
        for i in range(n):
            m *= n
        return m - (n - 1)


if __name__ == '__main__':
    print(Apples().getInitial(2))
