from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, Im the {script} script")
print("Id like to ask u a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of pc do u have {user_name}?")
computer = input(prompt)

print(f"""
ok, so you said {likes} about liking me.
You live in {lives}. Not sure where that is
And you have a {computer} computer. Nice.
""")
