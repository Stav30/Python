"""
p.406
Loop else
determine whether a positive integer y is prime by
1- assigning x the value of the second factor (2 is the first factor we check for) by using floor operator //
2- we're interested in non-imaginary numbers so use a while with x> 1 to loop through potential x factors
3- use modulus operator % to determine if x is a factor of y
4- if x is a factor use a break stmt to exit while loop
5- decrement x by 1, so we check for potential factors in descending order
Ideas for future git branched version:
- make 3 different test cases. Use a loop to test all.
"""
y = 5
x = y//2
while x > 1:
   if y%x == 0:
       print(y, 'has factor', x)
       break
   x-=1
else:
   print(y, 'is prime')
