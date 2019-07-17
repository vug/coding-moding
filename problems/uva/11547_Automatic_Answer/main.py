import sys


class U(object):
    """Utils."""

    @staticmethod
    def read_int():
        """Read one integer from stdin."""
        return int(sys.stdin.readline())

    @staticmethod
    def read_ints(sep=" "):
        """Read any number of integers from stdin."""
        return [int(s) for s in sys.stdin.readline().split(sep)]


def compute(num):
    """Multiply n by 567, then divide the result by 9, then add 7492,
    then multiply by 235, then divide by 47, then subtract 498.
    What is the digit in the tens column?"""
    # 567 / 9 = 63, 235 / 47 = 5
    num = (num * 63 + 7492) * 5 - 498
    if num < 0:  # modulus won't give correct result if number is negative
        num *= -1
    res = (num // 10) % 10
    return res


if __name__ == "__main__":
    t = U.read_int()
    for _ in range(t):
        n = U.read_int()
        print(compute(n))
