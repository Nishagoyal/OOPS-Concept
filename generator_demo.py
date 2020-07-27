def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])
print (my_nums)  #shows that it is a generator

print(my_nums.__next__())
print("hey")
#to access all values of yield :

for num in my_nums:
    print(num)




