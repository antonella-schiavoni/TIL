def substrCount(n, s):
    """
    :param n: the length of string s
    :int n:
    :param s: a string
    :str s:
    :return: The first line contains an integer, n, the length of s. The second line
    contains the strings.
    :rtype:
    """
    # Initialize total as n because each character is a palindrome substring
    total = n

    # List to store count of consecutive characters
    count_sequence = []
    i = 0

    # Traverse through given string
    while i < n:
        # Count of consecutive characters
        count = 1
        sequence_char = s[i]

        # Check for consecutive characters
        while i + 1 < n and s[i + 1] == sequence_char:
            i += 1
            count += 1

        # Store count of current consecutive sequence of characters
        count_sequence.append((sequence_char, count))
        i += 1

    # Case when all characters except the middle one are the same
    for i in range(1, len(count_sequence) - 1):
        if count_sequence[i - 1][0] == count_sequence[i + 1][0] and count_sequence[i][
            1] == 1:
            total += min(count_sequence[i - 1][1], count_sequence[i + 1][1])

    # Case when all characters are the same
    for i in range(len(count_sequence)):
        total += (count_sequence[i][1] * (count_sequence[i][1] - 1)) // 2

    return total


if __name__ == "__main__":
    s = "mnonopoo"
    print(substrCount(n=len(s), s=s))
