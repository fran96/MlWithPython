formatter = "{} {} {} {}"

'''formatter.format -->
    Tells python to:
        1. Take the formatter string defined above,
        2. Call its format function
        3. Pass to format 4 args which match up with the 4 {}
        in the formatter variable. (like passing args to the format func)
        4. The result of calling format on formatter is a new string that
        has the {} replaced with the four variables. This is what print is
        now printing out below.
'''
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song"
))
