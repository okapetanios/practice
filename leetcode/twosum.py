def twosum(nums, target):
    index_map = {}

    for i in range(len(nums)):
        num = nums[i]
        print("NUM:", num)
        twin = target - num
        print("TWIN:"+ str(twin))
        if twin in index_map:
            print([i,index_map.get(twin)])
            print(index_map)
            return
        index_map[num]=i
    print("No sum found\n")

a = [5,3,6,8,7]
twosum(a, 9)
        