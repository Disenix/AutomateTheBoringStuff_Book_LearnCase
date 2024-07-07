def a():
    print('a() starts')
    b() #➊
    d() #➋
    print('a() returns')

def b():
    print('b() starts')
    c() #➌
    print('b() returns')

def c():
    print('c() starts') #➍
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a() #➎
