n = int(input())
nums = list(map(int, input().split()))
newnums = []
for i in range(n):
    if nums[i] == 0:
        newnums.append(nums[i])
    elif nums[i] % 2 == 0:
        newnums.append(nums[i])
newnums.reverse()
for i in range(len(newnums)):
    print(newnums[i], end=' ')