from typing import Dict, List
from datetime import datetime


NUM_COUNT = 30000000


def puzzle1(numbers):
    S = Simulator(numbers)
    return S.run(NUM_COUNT)


class Simulator:

    def __init__(self, numbers):
        self.all_numbers = numbers
        self.last_utter = {num: [i] for i, num in enumerate(numbers)}

    def step(self):
        last_number = self.all_numbers[-1]
        if len(self.last_utter[last_number]) == 1:
            self.add_number(0)
        else:
            self.add_number(self.last_utter[last_number][-1] - self.last_utter[last_number][-2])

    def add_number(self, num):
        self.all_numbers.append(num)
        if num in self.last_utter:
            self.last_utter[num].append(len(self.all_numbers) - 1)
        else:
            self.last_utter[num] = [len(self.all_numbers) - 1]

    def run(self, turn_count):
        upto = turn_count - len(self.all_numbers)
        for i in range(upto):
            if i % 100000 == 0:
                print(i)
            self.step()
        print(self.all_numbers[-1])
        return self.all_numbers[-1]


# assert puzzle1([0, 3, 6]) == 175594
# assert puzzle1([1, 3, 2]) == 2578
# assert puzzle1([2, 1, 3]) == 3544142
t1 = datetime.now()
print(puzzle1([1, 0, 15, 2, 10, 13]))
print(datetime.now() - t1)
