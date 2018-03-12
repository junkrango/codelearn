file = open('newfile.txt', 'w')
file.write('I am created for the course. \n')
file.write('How about you? ')
file.write('How is your exam?')
file.close()
file = open('newfile.txt', 'r')
#show whole efile
print(file.read())
#show first ten characterrs
print(file.read(10))
#view by line
print(file.readline())
#view all by line
print(file.readlines())
file.close()