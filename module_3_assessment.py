Question 1
Fill in the blanks to print the numbers 1 through 7.
  

number = 1 # Initialize the variable
while number<=7: # Complete the while loop condition
    print(number, end=" ")
    number = number+1 # Increment the variable

# Should print 1 2 3 4 5 6 7 

---------------------------------------------------------

Question 2
 Find and correct the error in the for loop below.  The loop should check each number from 1 to 5 and identify if the number is odd or even. 

for number in range(5):
    if number % 2 == 0:
        print("odd")
    else:
        print("even")


# Should print:
# odd
# even
# odd
# even
# odd
-----------------------------------------------------------------------------------------------------------------------------------------------------
Question 3
Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. 

Tip: you can count the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
    count = 0
    if n == 0:
      count += 1
    while n != 0: # Complete the while loop condition
        # Complete the body of the while loop. This should include 
        # performing a calculation and incrementing a variable in the
        # appropriate order.  
        n = n // 10
        count = count + 1
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------




