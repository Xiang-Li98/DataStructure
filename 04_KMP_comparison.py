def get_next(t):
    """得到子串T的next数组"""
    i = 1
    j = 0
    t_next = [0]
    while i < len(t):
        if t[i] == t[j]:
            t_next.append(j + 1)
            i += 1
            j += 1
        else:
            if j == 0:
                t_next.append(0)
                i += 1
            else:
                j = t_next[j - 1]
    return t_next


def kmp_match(s, t):
    """KMP匹配"""
    t_next = get_next(t)
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = t_next[j - 1]
            else:
                i += 1
    if j == len(t):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    print(kmp_match("abcxabcdabcdabcy", "abcdabcy"))


