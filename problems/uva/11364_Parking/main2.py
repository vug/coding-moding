import sys


class Util(object):
    @staticmethod
    def read_int():
        """Read one integer from stdin."""
        return int(sys.stdin.readline())

    @staticmethod
    def read_ints(sep=' '):
        """Read any number of integers from stdin."""
        return [int(s) for s in sys.stdin.readline().split(sep)]


def min_dist(coords):
    """Get minimum travel distance given store coordinates."""
    coord_range = max(coords) - min(coords)  # maybe can implement a minmax method
    return 2 * coord_range


n_cases = Util.read_int()
for _ in range(n_cases):
    n_targets = Util.read_int()
    coords = Util.read_ints()
    print(min_dist(coords))
