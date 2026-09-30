from operator import truediv

language='java'
if language=='python':
    print('its python')
elif language =='java':
    print('its java')
else:
    print('not related')





user='admin'
login= True

if user=='admin'and login:
        print('login is true')
else:
        print('login is false')




if user=='admin' or login:
    print('random user login')
else:
    print('no login')



if not login:
    print('login is false')
else:
    print('login is true')


a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
print(id(a))
print(id(b))

a=[1,2,3]
a=b
print(a==b)
print(a is b)
print(id(a))
print(id(b))


