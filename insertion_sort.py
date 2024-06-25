nums=[6,9,1,3,2,10,5]

for i in range(1,len(nums)):
    j=i
    while(j>0 and nums[j-1]>nums[j]):

        nums[j-1], nums[j]= nums[j], nums[j-1]
        j=j-1

print(nums) 