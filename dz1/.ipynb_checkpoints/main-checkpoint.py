'''
Среднее геометрическое
count=0
res=1
nums=list(map(int,input().split()))
for i in range(len(nums)):
    res*=nums[i]
    count+=1
print(res**(1/count))
'''


'''
Перевод из одной СЧ в другую
N=int(input())
b=int(input())
c=int(input())
'''



#Номер 5
nums=list(map(int,input().split()))
nums[0],nums[len(nums)-1]=nums[len(nums)-1],nums[0]
print(nums)


#Номер 6
nums=list(map(int,input().split()))
res=0
for i in range(len(nums)):
    res=res^nums[i]
print(res)

#Номер 7
nums=list(map(int,input().split()))
for i in range(len(nums)):
    res=nums[1]
    if nums.count(nums[i])>nums.count(nums[1]):
        res=nums[i]
print(res)


#Номер 8
nums=list(map(int,input().split()))
med=0
for i in range(len(nums)):
    countless=0
    countmore=0
    for count in range(len(nums)):
        if (nums[i]>nums[count]):
            countmore+=1
        if (nums[i]<nums[count]):
            countless+=1
    if (countmore==countless):
        med=i
        break
print(nums[med])














