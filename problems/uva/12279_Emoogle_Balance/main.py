import sys

if __name__ == '__main__':
    k = 1
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        nums = [int(s) for s in sys.stdin.readline().split()]
        balance = sum([1 if x != 0 else -1 for x in nums])
        print("Case {}: {}".format(k, balance))
        k += 1
