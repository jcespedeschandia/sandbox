# Level 1
#1. 
x = 5
print(x)

#2.
x = 3
x = x+1
print(x)

#3.
x = 3
x = x+2
print(x+2)
print(x)

#4.
x = 3
x = x*x
print(x)
print(x*2)

#5.
x = 2
y = 5
z = x + y
print(z)

# Level 2
#1.
x = [1,2,4]
print(x)

#2.
x = [1,3,5]
print(x[0])

#3.
x = [2,4,6]
print(x[1])

#4.
x = [1,3,5]
print(x[2])

#5.
x = [1.3]
print(x[0])

#6.
x = [1,2,4]
x[0] = x[1]
print(x)

#7.
x = [1,3,5]
y = len(x)
print(y)

#8.
x = [2,4,6,3,7]
y = len(x) - 2
print(y)

#9.
x = [2,4,6,3,7]
y = len(x)
print(x[y-1])

#10.
x = [1,3,5,7]
x[0] = x[len(x) - 2]
print(x)

#11.
x = [1,3,5,7]
x[len(x) - 3] = x[int(len(x)/2) + int(len(x)/4)]
print(x)


#12.
x = [1,3,5,7]
y = [2,4,6]
x[2] = y[len(x) - 3]
print(x)

#13.
x = [1,3,5,7]
y = [2,4,6]
x[2] = y[len(x)-3] + x[x[0] + y[0]]
print(x)

# Level 3
#1.
x = [1,3,5]
x[0] = x[2]
x[1] = x[0]
print(x)

#2.
x = [1,3,5]
y = [0,5,7]
x[0] = x[1] + y[2]
y[1] = y[2] - x[0]
print(x)

#3.
x = [1,3,5,8]
x[0] = x[len(x) - 1]
print(x)

#4.
x = [1,3,5,8]
temp = x[len(x) - 1]
x[len(x) - 1] = x[0]
print(x)

#5.
x = [1,3,5,8]
x[len(x)-1],x[0] = x[0], x[len(x)-1]
print(x)

#6.
x = [1,3,5,8]
x.pop()
x.append(7)
print(x)

#7.
x = [1,3,5]
x[0] = 15
x.append(77)
print(x)

#8.
x = [1,3,5,8,2,-5,-8]
x[0] = x[len(x)-1]
x[len(x)-1] = x[0]
print(x)

#9.
x = [1,3,5,8,2,-5,-8]
x[len(x)-1], x[0] = x[0], x[len(x)-1]
print(x)

#10.
x = [1,3,5]
x.append(7)
print(x)

#11.
x = [2,4,6]
x.append(3)
print(x)

#12.
x = [1,3,5]
y = x[0] + x[1]
x.append(y)
print(x)

#13.
x = [2,3,5]
x.append(x[0] + x[1])
print(x)

#14.
x = [1,3,5]
x.pop()
print(x)

#15.
x = [1,3,5]
x.append(2)
x.pop()
print(x)
