import sys


class QuoteBeautifier(object):
    LEFT_SINGLE_QUOTES = "``"
    RIGHT_SINGLE_QUOTES = "''"

    def __init__(self):
        self.double_quote = QuoteBeautifier.LEFT_SINGLE_QUOTES

    def toggle(self):
        self.double_quote = (
            QuoteBeautifier.LEFT_SINGLE_QUOTES
            if self.double_quote == QuoteBeautifier.RIGHT_SINGLE_QUOTES
            else QuoteBeautifier.RIGHT_SINGLE_QUOTES
        )

    def beautify_line(self, line):
        out = []
        for char in line:
            if char != '"':
                out.append(char)
            else:
                out.append(self.double_quote)
                self.toggle()
        return "".join(out)


if __name__ == "__main__":
    qb = QuoteBeautifier()
    for line in sys.stdin.readlines():
        out = qb.beautify_line(line)
        sys.stdout.write(out)
