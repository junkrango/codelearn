str = input("enter a string\n")
def str_to_rts_version_1(str):
    return str[::-1]
rts_1 = str_to_rts_version_1(str)
print (rts_1)
def str_to_rts_version_2(str):
    result = list(str)
    result.reverse()
    a = "".join(result)
    return a
rts_2 = str_to_rts_version_2(str)
print (rts_2)



"""
切片
>>> m[:10]#取前十个数
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> m[-10:]#取后十个数
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> m[10:20]#取前11-20个数
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> m[:10:2]#前十个数中，每2个数取一个
[0, 2, 4, 6, 8]
>>> m[5:15:3]#第6-15个数中，每3个数取一个
[5, 8, 11, 14]
>>> m[::10]#所有的数中，每10个数取一个
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> m[:]#什么都不写，可以原样复制一个list
[0, 1, 2, 3, 4, 5, 6, 7,……,99]
"""
