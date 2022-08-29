
# Hashmap
def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    numsMap = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in numsMap:
            print([numsMap.get(val), i])
        numsMap[nums[i]] = i


# Bruteforce - worst solution, O(n)
def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    for x in range(len(nums)):
        for i in range(x+1, len(nums)):
            if nums[x] + nums[i] == target:
                print(x, i)
