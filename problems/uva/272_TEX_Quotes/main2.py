import sys


if __name__ == "__main__":
    is_left = True
    for char in sys.stdin.read():
        if char != '"':
            out = char
        else:
            out = "``" if is_left else "''"
            is_left = not is_left
        sys.stdout.write(out)
