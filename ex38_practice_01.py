ten_things = "Apples oranges crows telephone light sugar"

print("Wait there are not 10 things in that list, let's fix that.")
stuff = ten_things.title().split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
                "Banana", "Girl", "Boy"]

for i in range(0,10):
# while len(stuff) != 10:
    next_one = more_stuff.pop(i)
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")


print("There we go: ", stuff)

print("Let's do some things with stuff.")


print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))
