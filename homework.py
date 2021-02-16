import math
import sys

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

def squarePerimiter(sidelength):
    return sidelength * 4

def rectPerimiter(width, height):
    return 2 * (width + height)

def trianglePerimiter(side1, side2, side3):
    return side1 + side2 + side3

def squareArea(sidelength):
    return sidelength ** 2

def rectArea(width, height):
    return width * height

def triangleArea(base, height):
    return (base * height) / 2



while True:
    print('Mode 1: Power')
    print('Mode 2: Logarithm')
    print('Mode 3: Root')
    print('Mode 4: Hours to minutes')
    print('Mode 5: Hours to seconds')
    print('Mode 6: Minutes to hours')
    print('Mode 7: Minutes to seconds')
    print('Mode 8: Seconds to hours')
    print('Mode 9: Seconds to minutes')
    print('Mode 10: Perimiter (Square)')
    print('Mode 11: Perimiter (Rectangle)')
    print('Mode 12: Perimiter (Triangle)')
    print('Mode 13: Area (Square)')
    print('Mode 14: Area (Rectangle)')
    print('Mode 15: Area (Triangle)')


    mode = input('Mode: ')
    try:
        try:
            if int(mode) == 1:
                num = int(input('Number: '))
                exp = int(input('Power: '))
                print(power(num, exp))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try: 
            if int(mode) == 2:
                base = int(input('Base: '))
                res = int(input('Result: '))
                print(log(res, base))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 3:
                root = int(input('Root: '))
                num = int(input('Number to find root: '))
                print(findRoot(root, num))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 4:
                time = int(input('Time: '))
                print(hoursToMins(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 5:
                time = int(input('Time: '))
                print(hoursTosecs(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()

        try:
            if int(mode) == 6:
                time = int(input('Time: '))
                print(minsToHrs(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 7:
                time = int(input('Time: '))
                print(minsTosecs(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 8:
                time = int(input('Time: '))
                print(secsToHrs(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 9:
                time = int(input('Time: '))
                print(secsToMins(time))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 10:
                sidelength = int(input('Side Length: '))
                print(squarePerimiter(sidelength))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 11:
                width = int(input('Width: '))
                height = int(input('Height: '))
                print(rectPerimiter(width, height))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 12:
                side1 = int(input('Side 1: '))
                side2 = int(input('Side 2: '))
                side3 = int(input('Side 3: '))
                print(trianglePerimiter(side1, side2, side3))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 13:
                sidelength = int(input('Sidelength: '))
                print(squareArea(sidelength))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 14:
                width = int(input('Width: '))
                height = int(input('Height: '))
                print(rectArea(width, height))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
        try:
            if int(mode) == 15:
                base = int(input('Base: '))
                height = int(input('Height: '))
                print(triangleArea(base, height))
        except Exception as e:
            if '--debug' not in sys.argv:
                print('Something went wrong. Run with --debug to find a detailed error message.')
                exit()
            else:
                print(e)
                exit()
    except Exception as e:
        if '--debug' not in sys.argv:
            print(e)
            exit()
        else:
            print('Something went wrong. Run with --debug to find a detailed error message.')
            exit()
