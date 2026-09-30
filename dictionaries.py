student={'name':'RedJohn','age':'23','job':'murdering'}
print(student['name'])
print(student['age'])

print(student.get('phone ','not found'))

student['phone']='5555'
print(student)

student.update({'name':'lilnasX','age':'32','job':'babysitting'})
print(student)

del student['age']
print(student)

print(student.keys())
print(student.values())
print(student.items())
print(len(student))
