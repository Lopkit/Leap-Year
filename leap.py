# Code your functions here!

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.
def is_leap_year(year):
    if year%4 != 0:
        return False
    else:
        return True
print (is_leap_year(2020))
print(is_leap_year(2019))


# 2. Write a function that takes in the current year and returns a string telling when the next leap year will be.

def nextLeapYear(year):
    if year%4 == 0:
        return "It's a leap year!"
    else:
        remainingYears = year%4
        return str(remainingYears + year)
    
print (nextLeapYear(2020))
print (nextLeapYear(2019))

# 3. Write a function that takes in two years as arguments (a start_year and a last_year), and then prints out every single year between them that is a leap year. 

def leapsBetween(startYear, lastYear):
    x = range(startYear, lastYear)
    for i in x:
        if i%4 == 0:
            print (i)


print (leapsBetween(2005, 2021))
        
        
#or
        
def leapyears(startYear, lastYear):
    for x in range(startYear, lastYear):
        if x%4 ==0:
            print(x)

leapyears(2004, 2021)

#Second repost