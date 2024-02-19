num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
    print(fval)
    num = num + 1
    tot = tot + fval

print('ALL DONE')
print(tot, num, tot/num)

# max and min
max = None
nums = [18,94,15,8,44,100]
for num in nums:
    if max is None:
        max = num
    if max > num:
        max = num
print('Numbers:', nums, 'Max:', max)

min = None
nums2 = [176,54,5,38,44,6]
for num in nums2:
    if min is None:
        min = num
    if min < num:
        min = num
print('Numbers:', nums, 'Min:', min)