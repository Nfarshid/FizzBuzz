     def fizzBuzz(n)
     for fizzBuzz in range(1,n+1):
        if fizzBuzz % 15 == 0:
            print("FizzBuzz")
        if fizzBuzz%3==0 :
            print("Fizz")
        if fizzBuzz%5==0:
            print("Buzz")
        else:
            print(fizzBuzz)
       
