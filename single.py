def finding_single(nums):

    num_dict = {}
    for i in nums:
        if i in nums:
            num_dict[i] = nums.count(i)

    singles = [key for key, value in num_dict.items() if value == 1]

    return singles

print(finding_single([1, 1, 2, 2, 3]))