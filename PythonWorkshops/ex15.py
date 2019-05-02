from sys import argv

script, filename = argv

txt = open(filename)
close(txt)

print(f"Heres your file {filename}:")
print(txt.read())

print("Type the filename again pls: ")
file_again = input("> ")
txt_again = open(file_again)
close(txt_again)

print(txt_again.read())
