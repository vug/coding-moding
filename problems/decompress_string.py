"""
Question seen here
https://leetcode.com/discuss/interview-experience/124626/Google-onsite-interview-questions
"""


def decompress(s: str) -> str:
    r = []
    i = 0
    while i < len(s):
        # loop over characters, add them to result
        while i < len(s) and s[i].isalpha():
            r.append(s[i])
            i += 1
        if i == len(s):
            return ''.join(r)
        
        # loop over digits, parse them
        digits = []
        while s[i].isdigit():  # no fear of list bound violation
            digits.append(s[i])
            i += 1
        multiplier = int(''.join(digits))

        # get input of sub-problem
        n_open = 1
        j = i + 1
        sub_input = []
        while n_open > 0:
            sub_input.append(s[j])
            if s[j] == '[':
                n_open += 1
            elif s[j] == ']':
                n_open -= 1
            j += 1
        sub_res = decompress(s[i+1:j-1])  # don't include the close parenthesis
        r.extend(sub_res * multiplier)
        # jump current index to the end of sub-problem
        i = j

    result = ''.join(r)
    return result


if __name__ == '__main__':
    assert decompress('a') == 'a'
    assert decompress('abc') == 'abc'
    assert decompress('ab1[c]') == 'abc'
    assert decompress('ab2[c]') == 'abcc'
    assert decompress('ab2[cd]') == 'abcdcd'
    assert decompress('2[a]') == 'aa'
    assert decompress('2[a]b') == 'aab'
    assert decompress('a3[b2[c1[d]]]e') == 'abcdcdbcdcdbcdcde'
    assert decompress('a3[b]cde') == 'abbbcde'
    assert decompress('a2[bc]de2[fg]h') == 'abcbcdefgfgh'
    assert decompress('a2[b2[c]d]e2[f2[g]h]i') == 'abccdbccdefgghfgghi'
    assert decompress('a11[b]c') == 'abbbbbbbbbbbc'
