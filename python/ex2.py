# Exercise 2 - Magical Dates
def exercise2(day,month,year):
    if day * month == year % 100:
        return True
    else:
        return False

print(exercise2(3, 1, 1903))
print(exercise2(4, 2, 8))
print(exercise2(30, 3, 1990))
print(exercise2(1,1, 2000))
print(exercise2(5, 7,1940))

