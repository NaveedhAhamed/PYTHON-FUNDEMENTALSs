print('1 strings')

message = 'Living in Hopes'
print(message)

message = "Living's hope"
print(message)

print(len(message))
print(message[5])
print(message[3:11])
print(message.upper())
print(message.lower())
print(message.count('Living'))
print(message.count('i'))


print(message.find('hope'))
print(message.find('hopeless'))

message = message.replace('Living','mercy')
print(message)

name='lucy'
age='19'

print(name+' is ' +age + ' years old')

message='{} is {} years old'.format(name,age)
print(message)


