import pyautogui as gui
import time
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*/?"

user = lower_case + upper_case + number + symbol
length = 8

print('Valid request: random word, nonsense, script, count (type from 1 to n).')
try:
	option = input("Enter your request: ").lower()

	if option == 'script':
		filepath = str(input('Enter Filepath: '))
	else:
		number = round(float(input("Please type number: ")))


	time.sleep(5)

	if option == 'script':
		with open(str(filepath), 'r') as f:
			lines = f.readlines()
			for line in range(len(lines)):
				gui.write(lines[line])
	else:
		for i in range(number):
			password = "".join(random.sample(user,length))
			if option == "nonsense":
				gui.write(password)
			elif option == "count":
				gui.write(str(i+1) + '.')
			else:
				gui.write(option)
			gui.press('Enter')
	print('Troll Successfully')


except ValueError:
	print("Dude, please type number only!")

except Exception as e:
	print("Please try again.")
	print(e)

