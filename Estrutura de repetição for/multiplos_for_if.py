fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz += 1
        print("FizzBuzz")
    elif i % 3 == 0:
        fizz += 1
        print("Fizz")
    elif i % 5 == 0:
        buzz += 1
        print("Buzz")
    else:
        print(i)

print(f"A palavra Fizz apareceu {fizz}")
print(f"A palavra Buzz apareceu {buzz}")
print(f"A palavra FizzBuzz apareceu {fizzbuzz}")
