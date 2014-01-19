# Jacob Newman
# Working alongside the Textbook
# 9/20/2013

#print 5
#x=5
#print x+1

"""def right_justify(s):
    print (" " * (70 - len(s))) + s

right_justify("allen")

def do_twice(f,q):
    f(q) 
    f(q)

def print_twice(x):
    print x
import math

def do_four(p,b):
    p(b)
    p(b)

def take_cosine(b):
    print math.cos(b)

do_four(take_cosine, 1)

print 'and',
print 'but'

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

print bob

for i in range(4):
    fd(bob, 100)
    lt(bob)

for i in range(4):
    print 'Hello!'

wait_for_user()

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 25)

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

bob.delay = .05

def circle(t, r):
    circumference = 2 * math.pi * r
    n = (circumference/3) +1
    n= int(n)
    length = circumference/n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length / 3) +1
    step_length = arc_length/n
    step_angle = float(angle) / n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

wait_for_user()"""

def check_fermat(a,b,c,n):
    if (a**n+b**n == c**n):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def ask_user():
    a = int(raw_input('What\'s the value of a?\n'))
    b = int(raw_input('What\'s the value of b?\n'))
    c = int(raw_input('What\'s the value of c?\n'))
    n = int(raw_input('To what exponent?\n'))
    check_fermat(a,b,c,n)

def is_divisible(x,y):
    if x%y == 0:
        return True
    else:
        return False

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m, n-1))

def is_uniform(thelist):
    a = type(thelist[0])
    for x in range(len(thelist)):
        if not (type(thelist[x]) == a):
            return False
    return True


def replace(thelist,a,b):
    """Returns: a COPY of thelist but with all occurrences of a replaced by b. 
    
        Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].
        
    Precondition: thelist is a list of ints
                  a and b are ints"""
    copy = []
    for x in range(len(thelist)):
        if thelist[x] == a:
            copy.append(b)
        elif thelist[x] != a:
            copy.append(thelist[x])
    return copy

def square_root(a):
    epsilon = .000001
    x = float(a/2)
    while True:
        print x
        y = (x+a/x)/2
        if abs(y-x) < epsilon:
            break
        x = y

def nested_sum(thelist):
    total = 0
    for lists in thelist:
        total = total + sum(lists)
        # print total
    print total

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.upper())
    return res

def capitalize_nested(thelist):
    res = []
    for lists in thelist:
        res.append(capitalize_all(lists))
    return res

def cumulative_sum(thelist):
    res = []
    for index in range(len(thelist)):
        sublist = thelist[:index+1]
        total = sum(sublist)
        print total
        res.append(total)
    return res

def middle(thelist):
    copy = []
    copy.append(thelist[1:-1])
    return copy

def chop(thelist):
    del thelist[0]
    del thelist[-1]
    return None

def string_transposition(s):
    """Take a string, capitalize it, and rotate it 90 degrees."""
    for index in range(len(s)):
        print s[index].upper()
        

def histogram(s):
    """Returns a dictionary whose keys are the characters of s and whose values
    are the number of times that character appears in s"""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram1(s):
    """Trying to implement histogram using d.get. Unsuccesful"""
    d = dict()
    for c in s:
        d[c] = 0 + d.get(c, 1)
    return d

def sumall(*args):
    """A sum function that takes more than 2 arguments
    
    Precondition: args are ints"""
    counter = 0
    for number in args:
        counter += number
    return counter

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


def myLog(x,b):
    ans = 0
    for nums in range(x):
        if b**nums <= x:
            ans = nums
    return ans

def laceStrings(s1, s2):
    if len(s1) > len(s2):
        (s1, leftover) = (s1[0:len(s2)], s1[len(s2):])
    elif len(s1) < len(s2):
        (s2, leftover) = (s2[0:len(s1)], s2[len(s1):])
    else:
        leftover = ""
    
    chars = []
    for i in range(len(s1)):
        chars.append(s1[i])
        chars.append(s2[i])
    result = "".join(chars) + leftover
    return result

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    import math
    f = math.sqrt(f)
    guess = 1.0
    for i in range(100):
        if f(guess) - guess < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    sum = 0
    for width in range(start, stop, step):
        sum += f(float(width))
    return sum

def max_cols(table):
    result = table[0][:]
    print result
    for row in table:
        for k in range(len(row)):
            if row[k] > result[k]:
                result[k] = row[k]
    return result

def insert(thelist,x):
    if thelist == []:
        thelist.append(x)
    else:
        for pos in range(len(thelist)):
            if x <= thelist[pos]:
                thelist.insert(pos, x)
                x = max(thelist)+1
                
def mini(thelist):
    least = thelist[0]
    for x in thelist:
        if x < least:
            least = x
    return least

def sums(a,b):
    return a+b

def sum_in_loop(*args):
    count = 0
    for nums in args:
        count += nums
    return count




"""A game of 1-player battleship to be played at the interactive prompt.
Possibile improvements include a bigger board, hints to direct guesses, and
different sized battleships. This was created with guidaance from
Codeacademy.com's Python tutorial

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print "Turn: " + str(turn+1)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"
    print_board(board)"""















