import math

# MATH
print('All in one homework tool')
print('Always adding new features')

# Math functions ooga booga

# Exponents
def power(num, exp):
    return num ** exp

# Logarithms
def log(base, res):
    return math.log(base, res)

# Roots
def findRoot(root, num):
    return num**(1/float(root))

# Hours to minutes
def hoursToMins(time):
    return time * 60

# Hours to seconds
def hoursTosecs(time):
    return time * 60 * 60

# Minutes to hours
def minsToHrs(time):
    return time / 60

# Minutes to seconds
def minsTosecs(time):
    return time / 60

# Seconds to hours
def secsToHrs(time):
    return time * 60 * 60

# Seconds to minutes
def secsToMins(time):
    return time / 60


print('Mode 1: Power')
print('Mode 2: Logarithm')
print('Mode 3: Root')
print('Mode 4: Hours to minutes')
print('Mode 5: Hours to seconds')
print('Mode 6: Minutes to hours')
print('Mode 7: Minutes to seconds')
print('Mode 8: Seconds to hours')
print('Mode 9: Seconds to minutes')

mode = input('Mode: ')
try:
    if int(mode) == 1:
        num = int(input('Number: '))
        exp = int(input('Power: '))
        print(power(num, exp))
    elif int(mode) == 2:
        base = int(input('Base: '))
        res = int(input('Result: '))
        print(log(res, base))
    elif int(mode) == 3:
        root = int(input('Root: '))
        num = int(input('Number to find root: '))
        print(findRoot(root, num))
    elif int(mode) == 4:
        time = int(input('Time: '))
        print(hoursToMins(time))
    elif int(mode) == 5:
        time = int(input('Time: '))
        print(hoursTosecs(time))
    elif int(mode) == 6:
        time = int(input('Time: '))
        print(minsToHrs(time))
    elif int(mode) == 7:
        time = int(input('Time: '))
        print(minsTosecs(time))
    elif int(mode) == 8:
        time = int(input('Time: '))
        print(secsToHrs(time))
    elif int(mode) == 9:
        time = int(input('Time: '))
        print(secsToMins(time))
except:
    print('Unknown Error')
    exit()
