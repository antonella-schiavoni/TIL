from collections import defaultdict


class HitCounter:

    def __init__(self):
        self.hit_counter = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.hit_counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        ts_dif = timestamp - 300
        filter_from_ts = 0 if ts_dif < 0 else ts_dif
        filter_to_ts = filter_from_ts + 300

        counter_hits = 0
        for ts, hits in self.hit_counter.items():
            if filter_from_ts < ts <= filter_to_ts:
                counter_hits += self.hit_counter[ts]

        return counter_hits
      

if __name__ == '__main__':
    # Example run
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    print(obj.getHits(4)) # Expected 3
    obj.hit(300)
    print(obj.getHits(300)) # Expected 4
    print(obj.getHits(301)) # Expected 3
