# https://www.hackerrank.com/challenges/count-triplets-1/problem
import math
from collections import Counter

def is_geometric_progression(sub_arr, r):
    if len(sub_arr) != 3:
        return False

    if sub_arr[0] * r == sub_arr[1] and sub_arr[1] * r == sub_arr[2]:
        return True
    return False


def countTriplets(arr, r):
    counter = Counter(arr)
    counter_keys = list(counter.keys())
    result = 0
    if len(counter_keys) == 1:
        # si solo tengo una key, es el caso mas simple de combinatoria
        return math.comb(counter[counter_keys[0]], 3)
    for i in range(0, len(counter_keys)):
        keys_to_validate = counter_keys[i: i + 3]
        if len(keys_to_validate) == 3:
            if is_geometric_progression(keys_to_validate, r):
                # Obtener los valores correspondientes a esas keys que sean mayores a 0
                values = [counter[x] if counter[x] > 1 else 0 for x in keys_to_validate]
                if sum(values) == 0:
                    # significa que es una geometric progression pero de una sola ocurrencia
                    result += 1
                else:
                    result += sum(values)
    return result


if __name__ == '__main__':
    print(f"array: [1, 5, 25, 125], r: 5, result: {countTriplets([1, 5, 25, 125], 5)}")
    print(f"array: [1, 5, 5, 25, 125], r: 5, result:"
          f" {countTriplets([1, 5, 5, 25, 125], 5)}")
    print(f"array: [1, 3, 9, 9, 27, 81], r: 3, result:"
          f" {countTriplets([1, 3, 9, 9, 27, 81], 3)}")

    print(f"array: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,"
          f"1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], r: 1, result:{countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1)}")

    #assert is_geometric_progression([1, 5, 25], 5)
    #assert is_geometric_progression([1, 4, 16], 4)
    #assert(is_geometric_progression([1, 4, 9], 4), False)
