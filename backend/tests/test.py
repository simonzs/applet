from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        # one_list = list()
        two_list = list()
        three_list = nums
        result = list()
        for r_ind, three in enumerate(three_list):
            one_list = list()
            for w_ind, two in enumerate(two_list):
                one = 0 - two - three
                if one in one_list:
                    o_ind = one_list.index(one)
                    if o_ind != w_ind != r_ind:
                        # print("==============")
                        # print(one_list)
                        # print(two_list)
                        # print(three_list)
                        # print("==============")
                        result_one = [one, two, three]
                        result_one.sort()
                        if result_one not in result:
                            result.append(result_one)
                one_list.append(two)
            two_list.append(three)
        result.sort()
        return result

nums = [0,0,0]
nums = [-1,0,1,2,-1,-4]
r = threeSum(nums)
print(r)