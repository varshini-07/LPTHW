from sys import argv

script,user_name= argv
prompt =""

print(f"hi {user_name},i'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes=input(prompt)

print(f"wher do you live {user_name}?")
lives=input(prompt)

print("what kind of computer do you have ?")
computer=input(prompt)

print(f"""
alright,so you said {likes}about liking me.
you like in{lives}.not sure where that is.
and you have a {computer} computer.nice.
""")