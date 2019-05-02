

print("Choose a number to increment with")

def whileLoop(increment):
    i = 0
    x = 6
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

test = int(input("> "))

whileLoop(test)
