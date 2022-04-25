if __name__ == '__main__':
    for pos1 in range(1, 49):
        for pos2 in range(pos1 + 2, 49):
            nums = [i for i in range(1, 50)]
            nums[pos1] = nums[pos1] * nums[pos1 - 1]
            nums[pos1 - 1] = 0
            nums[pos2] = nums[pos2] * nums[pos2 - 1]
            nums[pos2 - 1] = 0
            if sum(nums) == 2015:
                print(f"pos1 = {pos1}, pos2 = {pos2}")
