def fizzbuzz(n):
    fizz = n % 3
    buzz = n % 5
    if (fizz == 0 and buzz !=0):
        n = "Fizz"
        return n
    elif (fizz != 0 and buzz ==0):
        n = "Buzz"
        return n
    elif (fizz == 0 and buzz ==0):
        n = "FizzBuzz"
        return n
    elif (fizz != 0 and buzz != 0):
        return n
