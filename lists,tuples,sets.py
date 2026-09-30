print('lists,tuples and sets')

print('lists')
courses=['history','maths','english','commerce']
print(courses[2:])
print(courses[:2])
print(courses[::2])
print(courses[::-1])

courses2=['science','geography']
print(courses2[:2])
print(courses2[::-1])
courses.extend(courses2)
print(courses)

courses.remove('history')
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses3= sorted(courses)
print(courses)

nums=['1','2','3','4','5','6','7','8','9']
print(min(nums))
print(max(nums))

nums_int = [int(x) for x in nums]
print(sum(nums_int))

for courses2 in courses:
    print(courses2)

for index,courses in enumerate(courses):
    print(courses)

    for index, courses in enumerate(courses,start=1):
        print(courses)

        courses_str='*'.join(courses)
        print(courses_str)

        newlist=courses_str.split('*')
        print(newlist)

        tuple1=('his','math','english','commerce')
        print(tuple1)



 mainscourses={'history','maths','english','commerce','science'}
 extrascourses={'japanese','english','commerce'}
 print(extrascourses.intersection(mainscourses))
 print(extrascourses.difference(mainscourses))
 print(mainscourses.union(extrascourses))
 



