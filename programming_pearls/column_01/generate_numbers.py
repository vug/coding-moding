"""
Script that generates N M-bit Integers and writes them into a file.

# problem input: took 10+ seconds, generated 85MB file
python generate_numbers.py --number-count 10 --upper-range 10
 --output-file "numbers_small.txt"

# small input
python generate_numbers.py --output-file "numbers_big.txt"
"""

import argparse
import random

if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Generate unique numbers in a range. Write them to a file."
    )
    ap.add_argument("--number-count", "-n", type=int, default=10_000_000)
    ap.add_argument("--upper-range", "-r", type=int, default=10_000_000)
    ap.add_argument("--output-file", "-o", type=str, default="numbers.txt")
    args = ap.parse_args()
    print("arguments:", args)

    assert (
        args.upper_range >= args.number_count
    ), "asking for more numbers than range will result in duplicates."

    whole_range = list(range(args.upper_range))
    random.shuffle(whole_range)  # in-place random order
    random_numbers = whole_range[: args.number_count]

    with open(args.output_file, "wt") as f:
        for n in random_numbers:
            f.write(f"{n}\n")
