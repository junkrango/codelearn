def log(func):
    def print_2():
        print("world")
        return func()
    return print_2
@log
def print_1():
    print ("hello")
print_1()
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2015-3-25')
# now()
