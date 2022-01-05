from typing import List, Set


def take_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [int(line) for line in lines]


def puzzle1(filepath):
    nums = take_input(filepath)
    num_ind = {}
    for i, num in enumerate(nums):
        if num not in num_ind:
            num_ind[num] = [i]
        else:
            num_ind[num].append(i)

    preamble = 25
    for ind in range(preamble, len(nums)):
        # print(f'checking {nums[ind]}')
        found = False
        for ind2 in range(ind-preamble, ind):
            # print(f'sum checking {nums[ind] - nums[ind2]}')
            comp = nums[ind] - nums[ind2]
            if comp in num_ind and ind2 != num_ind[comp] and any([ind2 <= x < ind for x in num_ind[comp]]):
                # print(f'found! {nums[ind2]} + {comp} = {nums[ind]} at {ind2} and {num_ind[comp]}')
                found = True
                break
        if not found:
            return nums[ind]


def puzzle2(filepath):
    nums = take_input(filepath)
    invalid_no = puzzle1(filepath)
    print(invalid_no)
    ptr1 = 0
    ptr2 = 1
    temp_sum = nums[ptr1] + nums[ptr2]
    while temp_sum != invalid_no:
        if temp_sum < invalid_no:
            ptr2 += 1
            temp_sum += nums[ptr2]
        elif temp_sum > invalid_no:
            ptr1 += 1
            temp_sum -= nums[ptr1 - 1]
    print(f'sum is {sum(nums[ptr1:ptr2+1])}')
    return min(nums[ptr1:ptr2 + 1]) + max(nums[ptr1:ptr2 + 1])


filepath = '/Users/hkoklu/personal/advent_of_code/2020/day09.txt'
print(puzzle1(filepath))
print(puzzle2(filepath))
