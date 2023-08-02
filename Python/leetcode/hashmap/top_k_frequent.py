from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    dict_counter = Counter(nums)  # Time complexity of O(n)
    most_common = dict_counter.most_common(k)  # Time complexity O(n log n) due to
    # sorting. Python has implemented most_common() in a way that allows it to
    # execute in O(n + k log n) time, which is more efficient when k < n.

    return [key for key, _ in most_common]


if __name__ == "__main__":
    print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
