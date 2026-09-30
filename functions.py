def hello_func():
    print("hello world")

hello_func() and print(hello_func())

def hello_func():
    return "hello world"
print(hello_func())


def hello_func(greeting,name='you'):
    return '{}, {}'.format(greeting,name)
print(hello_func("hello"))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('maths','art',name='john',age=22)


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Maths','English','History']
info = {'name':'john','age':22}

student_info(*courses, **info)




