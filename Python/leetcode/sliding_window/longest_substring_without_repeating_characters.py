def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    count = 0
    new = ''
    for i in s:
        if i not in new:
            new += i
        else:
            new = new[new.index(i) + 1:] + i
        if len(new) > count:
            count = len(new)
    return count


if __name__ == '__main__':
    s = "dvdf"
    print(lengthOfLongestSubstring(s))
