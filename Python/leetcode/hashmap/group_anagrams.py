def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic={}
    for word in strs:
        sorted_word="".join(sorted(word))
        if sorted_word not in dic:
            dic[sorted_word]=[word]
        else:
            dic[sorted_word].append(word)
    return dic.values()

if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams(["ddddddddddg", "dgggggggggg"]))
