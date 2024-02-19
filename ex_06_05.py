# Video 6.5 assignment is different from what the module 3 activities states it is (if I'm understanding correctly)
# Therefore, I'll be show code along for video and below will be the assignment from what's stated in module 3 activities

str = 'X-DSPAM-Confidence: 0.8475'
ipos = str.find(':')
piece = str[ipos+2:]
val = float(piece)
print(val)

# module 3 activities assignment
numbers = []
while True:
    uinput = input('Enter a number(once you are done picking numbers, type done): ')
    if uinput == 'done':
        break
    try:
        num = int(uinput)
        numbers.append(num)
    except ValueError:
        print('Invalid input')
if numbers:
    print('Max', max(numbers))
    print('Min', min(numbers))
else:
    print('No numbers entered.')