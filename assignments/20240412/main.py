def fizzbuzz(n: int) -> None:
    for i in range(n):
        if i % 15 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)
