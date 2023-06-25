# Repeat
# by cscheerer on GitHub

from time import sleep

print("Welcome!")
word = input("Thing to repeat: ")
time = input("Delay in seconds (cannot be a decimal but can be 0): ")
confirm = input("Type the password to confirm: ")
confirm = int(confirm)
confirm = 2469 * confirm

time = int(time)

while confirm == 12345:
    print(word)
    sleep(time)

print("sorry wrong passcode :|")