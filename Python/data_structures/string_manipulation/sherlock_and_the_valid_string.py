# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

from collections import Counter

from collections import Counter


def isValid(s):
  """
  The time complexity of the code is O(n), n is the length of the string. This is becasue we need to iterate over each character in the string when creating the frequency with counter.
  The space complexity of the code is O(n), since worst case scenario the counter object could end up storing each character in the string along with it's frequency.
  """
    # Get a frequency count of all characters in the string
    freq = Counter(s)

    # Get a frequency count of the frequencies
    freq_of_freq = Counter(freq.values())

    # If there's only one frequency, it's valid
    if len(freq_of_freq) == 1:
        return "YES"

    # If there are more than 2 frequencies, it's not valid
    elif len(freq_of_freq) > 2:
        return "NO"

    # If there are 2 frequencies:
    else:
        key1, key2 = freq_of_freq.keys()
        # If one of them is 1 and the frequency of 1 is also 1, it's valid
        if key1 == 1 and freq_of_freq[key1] == 1 or key2 == 1 and freq_of_freq[
            key2] == 1:
            return "YES"
        # If the frequencies differ by 1 and the frequency of the higher number is 1, it's valid
        elif abs(key1 - key2) == 1 and (
                freq_of_freq[key1] == 1 or freq_of_freq[key2] == 1):
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    # Test Cases
    # s = 'aabbcd'
    # s = 'aabbc'
    # s = 'abc'
    # s = 'aabbccddeefghi'
  
    s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'

    print(isValid(s))
