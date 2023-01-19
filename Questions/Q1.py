"""
Print each number from 1 to 100 on a new line.
For each multiple of 3, print "fizz" instead of numbers.
For each multiple of 5, print "buzz" instead of numbers.
For numbers that are multiples of both 3 and 5, print "fizzbuzz" instead of the number.
"""

# answer with list comprehension

res =['fizzbuzz' if i%3 == 0 and i%5 == 0  
     else 'fizz' if i%3 == 0 
     else 'buzz' if i%5 == 0 
     else i for i in range(1, 101)]
for nums in res:
    print(nums,"\n")
    
    
# answer with nested conditions

def fizzbuzz():
    for i in range(1, 101):
        if (i % 5) == 0 and (i % 3) == 0:
            print("fizzbuzz")
        elif (i % 3) == 0:
            print("fizz")
        elif (i % 5) == 0:
            print("buzz")
        else:
            print(i)
            
            
fizzbuzz()