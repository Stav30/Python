"""
p.405
Continue statement causes an immediate jump to the top of a loop.
Use continue to skip printing odd numbers
assign x = 10. decrement x by 1 inside while loop. use if + modulus+continue.
use end option with print to print even values: 8 6 4 2 0
"""
x = 10
while x:
    x-=1
    if x%2 != 0: continue
    print(x, end = ' ')
