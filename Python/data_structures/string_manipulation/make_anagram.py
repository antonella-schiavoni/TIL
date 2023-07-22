# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def makeAnagram(a, b):
    # Convert string to dictionaries
    dict_a = Counter(a)
    dict_b = Counter(b)
    deletions = 0

    # For each unique character from word a, check if it's present in dict_b. If it
    # is, then subtract the occurrences of char a in a with the occurrences of char
    # b, take the absolute value in case the substraction is negative. If the
    # character is not present in b, then we are sure that it's a string that we want
    # to delete
    for char in dict_a.keys():
        if char in dict_b.keys():
            deletions += abs(dict_a[char] - dict_b[char])
        else:
            deletions += dict_a[char]

    # Now it's turn to look at the keys from b, and if they are not in a, we need to 
    # delete them as they are redundant.
    for char in dict_b.keys():
        if char not in dict_a.keys():
            deletions += dict_b[char]

    return deletions


if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    print(makeAnagram(a, b))
