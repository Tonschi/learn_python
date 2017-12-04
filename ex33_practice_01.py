numbers = []

def PrintNumbers (limit, increment):
    i = 0
    for i in range(0,limit):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

PrintNumbers(50, 2.5)

print("The numbers: ")
for num in numbers:
    print(num)
