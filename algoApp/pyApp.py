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

# Level 4
#1.
counter = 1
if counter == 1:
    print('hello')

#2.
counter = 1
if counter == 1:
    print("hello")
elif counter == 2:
    print("world")

#3.
counter = 2
if counter < 10: 
    print("less than 10")
else: print("greater than or equal to 10")

#4.
counter = 1
if counter == 5:
    print("coding")
else: print("dojo")

#5.
x = [2,4,5]
counter = 0
if x[counter] < 5: 
    print("coding")
else: print("dojo")

#6.
x = [2,4,5]
counter = 2
if x[counter] > 10:
    print("coding")
else: print("dojo")

#7.
x = [2,4,5]
counter = 0

if x[counter] > 0: 
    print("coding")
    counter += 1
print(x[counter])

#8.
x = [2,4,5]
counter = 0

if x[counter] > 0: 
    print("coding")
    counter += 1
if x[counter] > 0: 
    print("coding")
    counter += 1
if x[counter] > 0: 
    print("coding")
    counter += 1

print(x)
print(counter)

# Level 5
#1.
for i in range(10):
    print(i)

#2.
x = 1

for i in range(3):
    x += 1
print(x)

#3.
x = 1
i = 0

while i < 3: 
    x += 1
    i+=1

print(x)
print(i)

#4.
x = 1
i = 0

while i <- 1:
    x = x + 1
    i += 1
print(x)

#5.
x = []
i = 0
while i < 10: 
    x.append(i*2)
    i+=1
print(x)

#_________

x = []
for i in range (10): 
    x.append(i*2)

print(x)

#6.
x = [1,3,5,8]

for i in range(len(x)):
    if x[i] > 4:
        x[i] = 0
print(x)

#_________

x = [1,3,5,8]
i = 0
while i < len(x): 
    if x[i] > 4:
        x[i] = 0
    i += 1
print(x)

#7.
x = [-1,3,2,7]

for i in range(len(x)):
    if x[i] < i: 
        x[i] = -10

print(x)

#_________

x = [-1,3,2,7]
i = 0
while i < len(x):
    if x[i] < i:
        x[i] = -10
    i += 1

print(x)

#8.
i = 20
while i != 10:
    print(i)
    i -= 1

#9.
x = 0
i = 1

while i < 4: 
    x += i
    print(x)
    print(i)
    i += 1

#10.
x = 0
i = 1

while i < 4: 
    x += i
    print(x)
    print(i)
    i += 2

# Level 6
#1.
def a():
    print(5)

a()

#2.
def a():
    print(55)


#3. (Error, en Javscript funciona pero en Python no)
a()
def a():
    print(25)

#4.
def a():
    b = 25
    b = b + 10
    print(b)

a()

#5.
def a(b,c):
    print(b)
    print(c)

a(3,5)

#6.
def a(b,c):
    return b + c

print(a(3,5))

#7.
def a(b,c):
    return b*c

print(a(3,5))

#8.
def a(b,c):
    return b*3-c

print(a(3,2))
print(a(1,1))

#9.
def a(b,c):
    return b+c

print(a(1,1) + a(2,2,))

#10.
def a(b,c):
    return b+c

print(a(1,a(2,3)))

#11.
def a(b,c):
    return b+c

print(a(a(1,2), a(2,3)))

#12.
def a(b,c):
    return b+c

print(a(a(1,2),a(2,a(1,2))))

#13.
def a(b,c):
    print(b)
    return b+c

print(a(3,2))

#14.
def a(b,c):
    print(c)
    return b-c

print(a(3,2))

#15.

def a():
    return 25
    return 50

print(a())

#16.
def a(b,c):
    return 25
    return b+c

print(a(3,2))


#17.
def a(b,c):
    return b+c

print(a(a(2,3), a(1,1)))

#18.
def a(b,c):
    return 0

print(a(a(2,3), a(1,1)))

# Level 7
#1.
i = 1
while i < 100: 
    if i==10:
        break
    print(i)
    i += 1

#2.
i = 13

while i<=20:
    if i == 50:
        break
    print(i)
    i += 1

#3.
i = 1;

while i <= 20:
    if i > 5:
        break
    else: print('hello')
    i += 1

#4.
i = 9

while i <= 20: 
    if i == 10:
        break
    else: print('hello')
    print(i)
    i += 1

#5.
message = 'CodingDojo'

i = 5
while i<=20:
    if i == len(message):
        break
    print(i)
    i+=1


