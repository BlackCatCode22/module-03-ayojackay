# CHAPTER 5
# num = 0
# while num > 0:
#     print(num)
#     num = num - 1
# print('Blastoff!')
# print(num)

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     print('Start')
#     line = input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done')

# for i in [5, 4, 3, 2, 1]:
#     if i == 2:
#         print('Malfunction issues...')
#         print('Wait, got it. Continue!')
#         print(i)
#         continue
#     print(i)
# print('Blastoff!')
# largest_so_far = -1
# print('Before', largest_so_far)
# for i in [10, 12, 3, 28, 89, 1, 0, 21]:
#     if i > largest_so_far:
#         largest_so_far = i
#     print(largest_so_far, i)
# print('After', largest_so_far)

# average
# count = 0
# summ = 0
# print('Before', 'count:', count, 'sum:', summ)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     summ = summ + value
#     print('Count:', count, 'Sum:', summ, 'Value:', value)
# print('After', 'count:', count, 'Sum:', summ, 'Average:', summ / count)

# filter
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large numebr', value)
# print('After')

#search using boolean
# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)

# smallest value
# smallest = None
# print('Before', smallest)
# for i in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = i
#     elif i < smallest:
#         smallest = i
#     print(smallest, i)
# print('After', smallest)

# CHAPTER 6
# string in loop
# word = 'mkay'
# for inx in word:
#     print('index', inx)
#     x = 3
#     w = word[x-1]
#     print('w', w)
# print('Done')

# string in loop 2
# word = 'awesome'
# for letter in word:
#     print('Give me a:', letter.upper(), '*clap clap*')
# print('What does that spell?', word.upper())

# slice
# sentence = 'okay friend'
# print(sentence[5:])
# print(sentence[:])
# print(sentence[0:4])
# print(sentence[5:10])

# stuff = 's'
# type(stuff)
# print(dir(stuff))

# fruit = 'apple'
# position = fruit.find('ry')
# if position == -1:
#     print('Whoops! That is not in our word.')
# else:
#     print('We are in the clear.')

# search and replace
# greet = 'Hello Jack'
# new_str = greet.replace('Jack', 'Jacque')
# print(new_str)
# new_str = new_str.replace('e', 'X')
# print(new_str)

# stripping white space
# greet = '        Hello Jacque '
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# prefixes
# line = 'Please have a nice day'
# print(line.startswith('Please'))
# print(line.startswith('P'))


