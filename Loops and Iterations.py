nums = [1,2,3,4,5,6]
for num in nums:
    if num == 3:
       print('found')
       break
    print(num)


nums = [1,2,3,4,5,6]
for num in nums:
    if num == 3:
       print('found')
       continue
    print(num)


for num in nums:
    for letter in 'abc':
        print(num,letter)


for num in range(1,11):
    print(num)


x=0
while x < 10:
    print(x)
    x += 1


x=0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

x=0
while True :
    if x == 5:
        break
    print(x)
    x += 1