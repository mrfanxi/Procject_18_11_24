def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        # print(i)
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            # print(j)
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]

print(bubbleSort(nums))
