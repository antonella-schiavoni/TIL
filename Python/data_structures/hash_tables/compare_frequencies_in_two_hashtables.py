# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    magazine_dict = Counter(magazine)
    note_dict = Counter(note)

    result = {}
    for key, value in note_dict.items():
        if key in magazine_dict.keys():
            magazine_dict[key] -= note_dict[key]
            result[key] = magazine_dict[key]
        else:
            print("No")
            return

    for key in note_dict.keys():
        if magazine_dict.get(key, -1) < 0:
            print("No")
            return
        
    print("Yes")
