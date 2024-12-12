num = int(input("input:"))
if  num % 3 == 0:
 print("Fizz")
elif num % 5 ==0:
  print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
 print("FizzBuzz")
else:
 print("[No Output]")